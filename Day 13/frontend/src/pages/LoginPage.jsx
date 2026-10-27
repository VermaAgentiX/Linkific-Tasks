import { useState } from "react";
import { Link, Navigate, useLocation, useNavigate } from "react-router-dom";
import { GraduationCap, LockKeyhole, Mail } from "lucide-react";
import { useAuth } from "../auth/AuthContext.jsx";

export default function LoginPage() {
  const { user, signIn } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  if (user) return <Navigate to="/" replace />;

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setBusy(true);
    try {
      await signIn(email, password);
      navigate(location.state?.from?.pathname || "/", { replace: true });
    } catch (err) {
      setError(err.message || "Unable to sign in.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="auth-page">
      <section className="auth-card">
        <div className="auth-brand-icon"><GraduationCap size={30} /></div>
        <p className="auth-eyebrow">STUDENT RECORD MANAGER</p>
        <h1>Welcome back</h1>
        <p className="auth-subtitle">Sign in to manage your student records.</p>
        <form onSubmit={handleSubmit} className="auth-form">
          <label className="form-field">
            Email address
            <span className="auth-input-wrap"><Mail size={17} /><input type="email" autoComplete="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="you@example.com" /></span>
          </label>
          <label className="form-field">
            Password
            <span className="auth-input-wrap"><LockKeyhole size={17} /><input type="password" autoComplete="current-password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter your password" /></span>
          </label>
          {error && <p className="error-message" role="alert">{error}</p>}
          <button className="button button-primary auth-submit" type="submit" disabled={busy}>
            {busy ? "Signing in…" : "Sign in"}
          </button>
        </form>
        <p className="auth-switch">New here? <Link to="/register">Create an account</Link></p>
        <p className="auth-footnote">Learning project · JWT access-token authentication</p>
      </section>
    </main>
  );
}
