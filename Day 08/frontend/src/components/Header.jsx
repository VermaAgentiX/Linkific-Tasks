import { GraduationCap, RefreshCw } from 'lucide-react';

export default function Header({ onRefresh, loading }) {
  return <header className="flex flex-col gap-4 border-b border-slate-200 bg-white px-5 py-5 sm:flex-row sm:items-center sm:justify-between sm:px-8">
    <div className="flex items-center gap-3">
      <div className="rounded-xl bg-blue-600 p-3 text-white"><GraduationCap size={25} /></div>
      <div><p className="text-xs font-bold uppercase tracking-[.2em] text-blue-600">Linkific · Day 7</p><h1 className="text-xl font-bold text-slate-900 sm:text-2xl">Student Record Manager</h1></div>
    </div>
    <button className="btn-secondary self-start sm:self-auto" onClick={onRefresh} disabled={loading}><RefreshCw size={16} className={loading ? 'animate-spin' : ''}/> Refresh records</button>
  </header>;
}
