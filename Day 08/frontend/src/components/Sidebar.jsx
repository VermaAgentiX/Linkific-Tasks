import { BookOpen, LayoutDashboard, Users } from 'lucide-react';

export default function Sidebar({ total, onShowAll }) {
  return <aside className="space-y-3">
    <div className="rounded-2xl bg-slate-900 p-5 text-white shadow-sm">
      <p className="text-xs font-semibold uppercase tracking-widest text-slate-400">Workspace</p>
      <div className="mt-4 flex items-center gap-3"><LayoutDashboard size={19}/><span className="font-semibold">Dashboard</span></div>
      <button onClick={onShowAll} className="mt-4 flex w-full items-center gap-3 rounded-xl bg-white/10 px-3 py-3 text-left text-sm hover:bg-white/15"><Users size={18}/> All students</button>
      <div className="mt-5 border-t border-white/10 pt-4"><p className="text-sm text-slate-400">Total records</p><p className="mt-1 text-3xl font-bold">{total}</p></div>
    </div>
    <div className="rounded-2xl border border-slate-200 bg-white p-4 text-sm text-slate-600"><div className="mb-2 flex items-center gap-2 font-semibold text-slate-800"><BookOpen size={17}/> Week 1 project</div><p>CRUD operations, search, form validation and API integration.</p></div>
  </aside>;
}
