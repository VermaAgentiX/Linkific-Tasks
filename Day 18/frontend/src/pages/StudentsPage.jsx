import StudentTable from "../components/StudentTable.jsx";

export default function StudentsPage({
  students,
  search,
  onSearchChange,
  onDelete,
  loading,
}) {
  return (
    <>
      <div className="page-heading">
        <p className="eyebrow-dark">RECORDS</p>
        <h1>All students</h1>
        <p>Search and manage all student records.</p>
      </div>

      <StudentTable
        students={students}
        search={search}
        onSearchChange={onSearchChange}
        onDelete={onDelete}
        loading={loading}
      />
    </>
  );
}
