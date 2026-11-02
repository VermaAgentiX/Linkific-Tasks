import { useEffect, useState } from "react";
import { ArrowLeft, Pencil } from "lucide-react";
import { Link, useParams } from "react-router-dom";

import { studentApi } from "../api.js";

export default function StudentDetailsPage() {
  const { id } = useParams();

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
    <section className="panel details-panel">
      <Link to="/students" className="back-link">
        <ArrowLeft size={16} /> Back to students
      </Link>

      <div className="details-heading">
        <div className="large-avatar">
          {student.name
            .split(" ")
            .map((part) => part[0])
            .slice(0, 2)
            .join("")
            .toUpperCase()}
        </div>

        <div className="details-title">
          <p className="eyebrow-dark">STUDENT ID #{student.id}</p>
          <h1>{student.name}</h1>
          <p>{student.course}</p>
        </div>

        <Link
          to={`/students/${student.id}/edit`}
          className="button button-primary"
        >
          <Pencil size={16} /> Edit record
        </Link>
      </div>

      <div className="details-grid">
        <div>
          <span>Age</span>
          <strong>{student.age}</strong>
        </div>
        <div>
          <span>Course</span>
          <strong>{student.course}</strong>
        </div>
        <div>
          <span>Email address</span>
          <strong>{student.email}</strong>
        </div>
      </div>
    </section>
  );
}
