import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="footer">
      <span>Built with React, React Router, Tailwind CSS and FastAPI</span>
      <Link to="/about">About this project</Link>
    </footer>
  );
}
