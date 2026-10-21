import { GraduationCap, UserRound, Users } from 'lucide-react';
import StudentForm from './StudentForm.jsx';
import StudentTable from './StudentTable.jsx';

export default function Content(props) {
  const { students, allStudents, query, setQuery, editing, onSave, onCancel, onEdit, onDelete, loading, saving } = props;
  return <main className="min-w-0 space-y-6">
    <div><p className="text-sm font-medium text-blue-600">Overview / Students</p><h2 className="mt-1 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">Your student dashboard</h2><p className="mt-2 text-slate-500">Manage student information from one simple workspace.</p></div>
    <div className="grid gap-4 sm:grid-cols-3">
      <div className="stat-card"><div className="stat-icon bg-blue-50 text-blue-700"><Users size={20}/></div><p className="stat-label">Total students</p><p className="stat-value">{allStudents.length}</p></div>
      <div className="stat-card"><div className="stat-icon bg-violet-50 text-violet-700"><GraduationCap size={20}/></div><p className="stat-label">Courses represented</p><p className="stat-value">{new Set(allStudents.map(st => st.course.toLowerCase())).size}</p></div>
      <div className="stat-card"><div className="stat-icon bg-emerald-50 text-emerald-700"><UserRound size={20}/></div><p className="stat-label">Average age</p><p className="stat-value">{allStudents.length ? Math.round(allStudents.reduce((sum, st) => sum + st.age, 0) / allStudents.length) : '—'}</p></div>
    </div>
    <StudentForm editing={editing} onSave={onSave} onCancel={onCancel} saving={saving}/>
    <StudentTable students={students} query={query} setQuery={setQuery} onEdit={onEdit} onDelete={onDelete} loading={loading}/>
  </main>;
}
