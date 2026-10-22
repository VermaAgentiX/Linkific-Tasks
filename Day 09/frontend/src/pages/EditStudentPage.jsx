import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { studentApi } from "../api.js";
import StudentForm from "../components/StudentForm.jsx";

export default function EditStudentPage({ onUpdate }) {
  const { id } = useParams();
  const navigate = useNavigate();

  const [student, setStudent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isCurrent = true;

    async function loadStudent() {
      setLoading(true);
      setError("");

      try {
        const data = await studentApi.getById(id);

        if (isCurrent) {
          setStudent(data);
        }
      } catch (loadError) {
        if (isCurrent) {
          setError(loadError.message);
        }
      } finally {
        if (isCurrent) {
          setLoading(false);
        }
      }
    }

    loadStudent();

    return () => {
      isCurrent = false;
    };
  }, [id]);

  async function handleUpdate(studentData) {
    await onUpdate(Number(id), studentData);
    navigate(`/students/${id}`);
  }

  if (loading) {
    return <section className="panel">Loading student details...</section>;
  }

  if (error) {
    return (
      <section className="panel">
        <p className="error-message">{error}</p>
        <Link to="/students" className="text-link">
          Back to students
        </Link>
      </section>
    );
  }

  return (
    <>
      <div className="page-heading">
        <p className="eyebrow-dark">RECORDS / EDIT</p>
        <h1>Edit student</h1>
        <p>Update the record and save your changes.</p>
      </div>

      <StudentForm
        initialStudent={student}
        onSave={handleUpdate}
        buttonLabel="Save changes"
      />
    </>
  );
}
