import { BookOpen, Sparkles } from 'lucide-react'

export default function Header() {
  return (
    <header className="topbar">
      <a className="brand" href="#top" aria-label="React Basics Lab home">
        <span className="brand-icon"><Sparkles size={18} /></span>
        <span>React Basics <span className="brand-accent">Lab</span></span>
      </a>
      <a className="top-link" href="#topics"><BookOpen size={16} /> Revision topics</a>
    </header>
  )
}
