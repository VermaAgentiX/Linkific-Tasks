import { Link } from "react-router-dom";
import { ShieldAlert } from "lucide-react";
export default function UnauthorizedPage() {
  return <main className="auth-page"><section className="auth-card">
    <div className="auth-brand-icon"><ShieldAlert size={30}/></div>
    <p className="auth-eyebrow">ACCESS DENIED</p><h1>403 · Unauthorized</h1>
    <p className="auth-subtitle">Your account does not have permission to view this page.</p>
    <Link className="button button-primary auth-submit" to="/">Return to dashboard</Link>
  </section></main>;
}
