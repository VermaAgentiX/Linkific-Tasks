import { useNavigate } from "react-router-dom";

import StudentForm from "../components/StudentForm.jsx";

export default function AddStudentPage({ onCreate }) {
  const navigate = useNavigate();

  async function handleCreate(studentData) {
    await onCreate(studentData);
    navigate("/students");
  }

  return (
    <>
      <div className="page-heading">
        <p className="eyebrow-dark">RECORDS / NEW</p>
        <h1>Add a student</h1>
        <p>Create a new student record using the FastAPI backend.</p>
      </div>

      <StudentForm onSave={handleCreate} buttonLabel="Create student" />
    </>
  );
}
