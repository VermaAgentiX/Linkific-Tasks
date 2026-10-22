import { LayoutDashboard, Users, UserPlus, BookOpen } from "lucide-react";
import { NavLink } from "react-router-dom";

export default function Sidebar({ totalStudents }) {
  return (
    <aside className="sidebar">
      <p className="sidebar-label">WORKSPACE</p>

      <NavLink to="/" end className="sidebar-link">
        <LayoutDashboard size={18} />
        Dashboard
      </NavLink>

      <NavLink to="/students" className="sidebar-link">
        <Users size={18} />
        All students
      </NavLink>

      <NavLink to="/students/new" className="sidebar-link">
        <UserPlus size={18} />
        Add student
      </NavLink>

      <div className="sidebar-total">
        <span>Total records</span>
        <strong>{totalStudents}</strong>
      </div>

      <div className="sidebar-note">
        <BookOpen size={18} />
        <strong>Day 9 learning</strong>
        <p>React Hooks, routing, API data, and CRUD operations.</p>
      </div>
    </aside>
  );
}
