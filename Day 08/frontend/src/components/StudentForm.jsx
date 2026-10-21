import { useEffect, useState } from 'react';
import { Save, X } from 'lucide-react';

const empty = { name: '', age: '', course: '', email: '' };

export default function StudentForm({ editing, onSave, onCancel, saving }) {
  const [form, setForm] = useState(empty);
  const [error, setError] = useState('');

  useEffect(() => {
    setForm(editing ? { name: editing.name, age: String(editing.age), course: editing.course, email: editing.email } : empty);
    setError('');
  }, [editing]);

  function change(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function submit(e) {
    e.preventDefault();
    if (!form.name.trim() || !form.course.trim() || !form.email.trim() || !form.age) {
      setError('Please complete every field.');
      return;
    }
    if (Number(form.age) < 1 || Number(form.age) > 120) {
      setError('Age must be between 1 and 120.');
      return;
    }
    try {
      setError('');
      await onSave({ name: form.name.trim(), age: Number(form.age), course: form.course.trim(), email: form.email.trim() });
      if (!editing) setForm(empty);
    } catch (err) {
      setError(err.message);
    }
  }

  return <form onSubmit={submit} className="card">
    <div className="mb-5 flex items-start justify-between"><div><h2 className="section-title">{editing ? 'Edit student' : 'Add a student'}</h2><p className="mt-1 text-sm text-slate-500">{editing ? `Updating record #${editing.id}` : 'Create a new student record.'}</p></div>{editing && <button type="button" className="icon-btn" onClick={onCancel} aria-label="Cancel edit"><X size={18}/></button>}</div>
    <div className="grid gap-4 sm:grid-cols-2">
      <label className="field-label">Full name<input className="field-input" name="name" value={form.name} onChange={change} placeholder="e.g. Aditi Sharma" minLength="2" maxLength="80" required /></label>
      <label className="field-label">Age<input className="field-input" name="age" type="number" min="1" max="120" value={form.age} onChange={change} placeholder="e.g. 21" required /></label>
      <label className="field-label">Course<input className="field-input" name="course" value={form.course} onChange={change} placeholder="e.g. Computer Science" minLength="2" maxLength="100" required /></label>
      <label className="field-label">Email<input className="field-input" name="email" type="email" value={form.email} onChange={change} placeholder="student@example.com" maxLength="120" required /></label>
    </div>
    {error && <p role="alert" className="mt-4 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">{error}</p>}
    <div className="mt-5 flex flex-wrap gap-2"><button className="btn-primary" type="submit" disabled={saving}><Save size={16}/>{saving ? 'Saving…' : editing ? 'Save changes' : 'Add student'}</button>{editing && <button className="btn-secondary" type="button" onClick={onCancel}>Cancel</button>}</div>
  </form>;
}
