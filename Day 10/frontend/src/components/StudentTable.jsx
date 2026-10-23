import { Eye, Pencil, Search, Trash2 } from "lucide-react";
import { Link } from "react-router-dom";

export default function StudentTable({
  students,
  search,
  onSearchChange,
  onDelete,
  loading,
}) {
  return (
    <section className="panel">
      <div className="panel-toolbar">
        <div className="panel-heading">
          <h2>Student records</h2>
          <p>Search, view, edit, or delete a student record.</p>
        </div>

        <label className="search-box">
          <Search size={17} />
          <input
            value={search}
            onChange={(event) => onSearchChange(event.target.value)}
            placeholder="Search students..."
            aria-label="Search students"
          />
        </label>
      </div>

      <div className="table-scroll">
        <table className="student-table">
          <thead>
            <tr>
              <th>Student</th>
              <th>Age</th>
              <th>Course</th>
              <th>Email</th>
              <th className="actions-heading">Actions</th>
            </tr>
          </thead>

          <tbody>
            {students.map((student) => (
              <tr key={student.id}>
                <td>
                  <strong>{student.name}</strong>
                  <small>Student ID #{student.id}</small>
                </td>
                <td>{student.age}</td>
                <td>{student.course}</td>
                <td>{student.email}</td>
                <td>
                  <div className="table-actions">
                    <Link
                      className="action-button"
                      to={`/students/${student.id}`}
                      aria-label={`View ${student.name}`}
                      title="View student"
                    >
                      <Eye size={16} />
                    </Link>
                    <Link
                      className="action-button"
                      to={`/students/${student.id}/edit`}
                      aria-label={`Edit ${student.name}`}
                      title="Edit student"
                    >
                      <Pencil size={16} />
                    </Link>
                    <button
                      className="action-button delete-action"
                      onClick={() => onDelete(student)}
                      aria-label={`Delete ${student.name}`}
                      title="Delete student"
                    >
                      <Trash2 size={16} />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {loading && <p className="table-message">Loading student records...</p>}

      {!loading && students.length === 0 && (
        <div className="empty-state">
          <Search size={28} />
          <strong>No students found</strong>
          <p>Try a different search or add a new student record.</p>
        </div>
      )}
    </section>
  );
}
