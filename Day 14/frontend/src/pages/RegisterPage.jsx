import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { GraduationCap, LockKeyhole, Mail, UserRound } from "lucide-react";
import { useAuth } from "../auth/AuthContext.jsx";

export default function RegisterPage() {
  const { user, signUp } = useAuth();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();

  if (user) return <Navigate to="/" replace />;

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setBusy(true);
    try {
      await signUp(name, email, password);
      navigate("/", { replace: true });
    } catch (err) {
      setError(err.message || "Unable to create account.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="auth-page">
      <section className="auth-card">
        <div className="auth-brand-icon"><GraduationCap size={30} /></div>
        <p className="auth-eyebrow">STUDENT RECORD MANAGER</p>
        <h1>Create your account</h1>
        <p className="auth-subtitle">Register to access the student workspace.</p>
        <form onSubmit={handleSubmit} className="auth-form">
          <label className="form-field">
            Full name
            <span className="auth-input-wrap"><UserRound size={17} /><input type="text" autoComplete="name" minLength="2" maxLength="80" required value={name} onChange={e => setName(e.target.value)} placeholder="Your name" /></span>
          </label>
          <label className="form-field">
            Email address
            <span className="auth-input-wrap"><Mail size={17} /><input type="email" autoComplete="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="you@example.com" /></span>
          </label>
          <label className="form-field">
            Password
            <span className="auth-input-wrap"><LockKeyhole size={17} /><input type="password" autoComplete="new-password" minLength="8" maxLength="128" required value={password} onChange={e => setPassword(e.target.value)} placeholder="At least 8 characters" /></span>
          </label>
          {error && <p className="error-message" role="alert">{error}</p>}
          <button className="button button-primary auth-submit" type="submit" disabled={busy}>
            {busy ? "Creating account…" : "Create account"}
          </button>
        </form>
        <p className="auth-switch">Already registered? <Link to="/login">Sign in</Link></p>
        <p className="auth-footnote">Passwords are hashed on the backend, not stored as plain text.</p>
      </section>
    </main>
  );
}
