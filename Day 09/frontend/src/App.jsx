import { useCallback, useEffect, useState } from "react";
import { Route, Routes, useLocation } from "react-router-dom";
import { AlertCircle, CheckCircle2, X } from "lucide-react";

import { studentApi } from "./api.js";
import Header from "./components/Header.jsx";
import Sidebar from "./components/Sidebar.jsx";
import Footer from "./components/Footer.jsx";
import DashboardPage from "./pages/DashboardPage.jsx";
import StudentsPage from "./pages/StudentsPage.jsx";
import AddStudentPage from "./pages/AddStudentPage.jsx";
import EditStudentPage from "./pages/EditStudentPage.jsx";
import StudentDetailsPage from "./pages/StudentDetailsPage.jsx";
import AboutPage from "./pages/AboutPage.jsx";
import NotFoundPage from "./pages/NotFoundPage.jsx";

export default function App() {
  const [allStudents, setAllStudents] = useState([]);
  const [visibleStudents, setVisibleStudents] = useState([]);
  const [stats, setStats] = useState(null);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [notice, setNotice] = useState(null);

  const location = useLocation();

  const loadDashboardData = useCallback(async (searchTerm = search) => {
    setLoading(true);

    try {
      const [allRecords, filteredRecords, dashboardStats] = await Promise.all([
        studentApi.getAll(),
        studentApi.getAll(searchTerm),
        studentApi.getStats(),
      ]);

      setAllStudents(allRecords);
      setVisibleStudents(filteredRecords);
      setStats(dashboardStats);
    } catch (error) {
      setNotice({
        type: "error",
        message: `${error.message}. Make sure the FastAPI backend is running on port 8000.`,
      });
    } finally {
      setLoading(false);
    }
  }, [search]);

  // Load initial data when the application starts.
  useEffect(() => {
    loadDashboardData("");
  }, []);

  // Refresh the filtered list when the search text changes.
  useEffect(() => {
    const timerId = window.setTimeout(() => {
      loadDashboardData(search);
    }, 250);

    return () => window.clearTimeout(timerId);
  }, [search, loadDashboardData]);

  // Start each new page at the top.
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [location.pathname]);

  async function handleCreate(studentData) {
    await studentApi.create(studentData);
    setNotice({ type: "success", message: "Student created successfully." });
    await loadDashboardData(search);
  }

  async function handleUpdate(studentId, studentData) {
    await studentApi.update(studentId, studentData);
    setNotice({ type: "success", message: "Student updated successfully." });
    await loadDashboardData(search);
  }

  async function handleDelete(student) {
    const shouldDelete = window.confirm(
      `Delete the record for ${student.name}? This action cannot be undone.`
    );

    if (!shouldDelete) {
      return;
    }

    try {
      await studentApi.remove(student.id);
      setNotice({ type: "success", message: "Student deleted successfully." });
      await loadDashboardData(search);
    } catch (error) {
      setNotice({ type: "error", message: error.message });
    }
  }

  const isAboutPage = location.pathname === "/about";

  return (
    <div className="app">
      <Header />

      <div className="app-layout">
        {!isAboutPage && (
          <Sidebar totalStudents={allStudents.length} />
        )}

        <main className="page-content">
          {notice && (
            <div
              className={`status-message status-${notice.type}`}
              role="status"
            >
              {notice.type === "error" ? (
                <AlertCircle size={18} />
              ) : (
                <CheckCircle2 size={18} />
              )}

              <span>{notice.message}</span>

              <button
                className="dismiss-button"
                onClick={() => setNotice(null)}
                aria-label="Dismiss notification"
              >
                <X size={17} />
              </button>
            </div>
          )}

          <Routes>
            <Route
              path="/"
              element={
                <DashboardPage
                  students={allStudents}
                  stats={stats}
                  loading={loading}
                />
              }
            />

            <Route
              path="/students"
              element={
                <StudentsPage
                  students={visibleStudents}
                  search={search}
                  onSearchChange={setSearch}
                  onDelete={handleDelete}
                  loading={loading}
                />
              }
            />

            <Route
              path="/students/new"
              element={<AddStudentPage onCreate={handleCreate} />}
            />

            <Route
              path="/students/:id"
              element={<StudentDetailsPage />}
            />

            <Route
              path="/students/:id/edit"
              element={<EditStudentPage onUpdate={handleUpdate} />}
            />

            <Route path="/about" element={<AboutPage />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </main>
      </div>

      <Footer />
    </div>
  );
}
