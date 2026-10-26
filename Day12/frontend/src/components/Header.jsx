import { GraduationCap } from "lucide-react";
import { Link, NavLink } from "react-router-dom";

const getNavClass = ({ isActive }) =>
  `nav-link${isActive ? " nav-link-active" : ""}`;

export default function Header() {
  return (
    <header className="topbar">
      <Link to="/" className="brand">
        <span className="brand-icon">
          <GraduationCap size={25} />
        </span>

        <span>
          <small>LINKIFIC · DAY 9</small>
          <strong>Student Record Manager</strong>
        </span>
      </Link>

      <nav className="main-nav" aria-label="Main navigation">
        <NavLink to="/" end className={getNavClass}>
          Dashboard
        </NavLink>
        <NavLink to="/students" className={getNavClass}>
          Students
        </NavLink>
        <NavLink to="/students/new" className={getNavClass}>
          Add student
        </NavLink>
        <NavLink to="/about" className={getNavClass}>
          About
        </NavLink>
      </nav>
    </header>
  );
}
