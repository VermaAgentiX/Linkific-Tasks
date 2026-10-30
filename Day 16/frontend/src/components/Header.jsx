import { GraduationCap, LogOut } from "lucide-react";
import { useAuth } from "../auth/AuthContext.jsx";
import { Link, NavLink } from "react-router-dom";

const getNavClass = ({ isActive }) =>
  `nav-link${isActive ? " nav-link-active" : ""}`;

export default function Header() {
  const { user, signOut } = useAuth();

  return (
    <header className="topbar">
      <Link to="/" className="brand">
        <span className="brand-icon">
          <GraduationCap size={25} />
        </span>

        <span>
          <small>LINKIFIC · DAY 15</small>
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
        {user?.role === "admin" && <NavLink to="/admin" className={getNavClass}>Admin</NavLink>}
      </nav>

      <div className="account-menu">
        <span className="account-name">{user?.name || user?.email} <span className={`role-pill role-${user?.role || "user"}`}>{user?.role || "user"}</span></span>
        <button className="button button-signout" onClick={signOut} type="button">
          <LogOut size={15} /> Sign out
        </button>
      </div>
    </header>
  );
}
