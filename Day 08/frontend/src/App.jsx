import { useCallback, useEffect, useState } from 'react';
import { AlertCircle, CheckCircle2 } from 'lucide-react';
import { api } from './api.js';
import Header from './components/Header.jsx';
import Sidebar from './components/Sidebar.jsx';
import Content from './components/Content.jsx';
import Footer from './components/Footer.jsx';

export default function App() {
  const [allStudents, setAllStudents] = useState([]);
  const [students, setStudents] = useState([]);
  const [query, setQuery] = useState('');
  const [editing, setEditing] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [notice, setNotice] = useState(null);

  const loadStudents = useCallback(async (term = query) => {
    setLoading(true);
    try {
      const [filtered, all] = await Promise.all([api.list(term), api.list()]);
      setStudents(filtered);
      setAllStudents(all);
    } catch (err) {
      setNotice({ type: 'error', text: `${err.message}. Is the FastAPI server running on port 8000?` });
    } finally {
      setLoading(false);
    }
  }, [query]);

  useEffect(() => { loadStudents(''); }, []); // Initial load
  useEffect(() => {
    const timer = setTimeout(() => loadStudents(query), 250);
    return () => clearTimeout(timer);
  }, [query, loadStudents]);

  async function saveStudent(data) {
    setSaving(true);
    try {
      if (editing) {
        await api.update(editing.id, data);
        setNotice({ type: 'success', text: 'Student record updated.' });
      } else {
        await api.create(data);
        setNotice({ type: 'success', text: 'Student record created.' });
      }
      setEditing(null);
      await loadStudents(query);
    } finally {
      setSaving(false);
    }
  }

  async function deleteStudent(st) {
    if (!window.confirm(`Delete ${st.name}'s record? This cannot be undone.`)) return;
    try {
      await api.remove(st.id);
      if (editing?.id === st.id) setEditing(null);
      setNotice({ type: 'success', text: 'Student record deleted.' });
      await loadStudents(query);
    } catch (err) {
      setNotice({ type: 'error', text: err.message });
    }
  }

  return <div className="min-h-screen bg-slate-50">
    <Header onRefresh={() => loadStudents(query)} loading={loading}/>
    <div className="mx-auto grid max-w-[1500px] gap-6 px-4 py-7 sm:px-6 lg:grid-cols-[250px_minmax(0,1fr)] lg:px-8">
      <Sidebar total={allStudents.length} onShowAll={() => setQuery('')}/>
      <div className="min-w-0">
        {notice && <div role="status" className={`mb-5 flex items-start gap-2 rounded-xl border px-4 py-3 text-sm ${notice.type === 'error' ? 'border-red-200 bg-red-50 text-red-700' : 'border-emerald-200 bg-emerald-50 text-emerald-700'}`}>{notice.type === 'error' ? <AlertCircle size={18}/> : <CheckCircle2 size={18}/>}<span className="flex-1">{notice.text}</span><button onClick={() => setNotice(null)} aria-label="Dismiss message" className="font-bold">×</button></div>}
        <Content students={students} allStudents={allStudents} query={query} setQuery={setQuery} editing={editing} onSave={saveStudent} onCancel={() => setEditing(null)} onEdit={setEditing} onDelete={deleteStudent} loading={loading} saving={saving}/>
      </div>
    </div>
    <Footer/>
  </div>;
}
