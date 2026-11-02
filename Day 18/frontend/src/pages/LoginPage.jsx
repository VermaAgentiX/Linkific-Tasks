import { useState } from "react";
import { Link, Navigate, useLocation, useNavigate } from "react-router-dom";
import { GraduationCap, LockKeyhole, Mail } from "lucide-react";
import { useAuth } from "../auth/AuthContext.jsx";

export default function LoginPage() {
  const { user, signIn } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [fieldErrors, setFieldErrors] = useState({});
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  if (user) return <Navigate to="/" replace />;

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    const nextErrors = {};
    if (!email.trim()) nextErrors.email = "Email address is required.";
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim())) nextErrors.email = "Enter a valid email address.";
    if (!password) nextErrors.password = "Password is required.";
    setFieldErrors(nextErrors);
    if (Object.keys(nextErrors).length) return;
    setBusy(true);
    try {
      await signIn(email.trim().toLowerCase(), password);
      navigate(location.state?.from?.pathname || "/", { replace: true });
    } catch (err) {
      setFieldErrors(err.fieldErrors || {});
      setError(err.message || "Unable to sign in. Please try again.");
    } finally { setBusy(false); }
  }

  return (
    <main className="auth-page"><section className="auth-card">
      <div className="auth-brand-icon"><GraduationCap size={30} /></div>
      <p className="auth-eyebrow">STUDENT RECORD MANAGER</p><h1>Welcome back</h1>
      <p className="auth-subtitle">Sign in to manage your student records.</p>
      <form onSubmit={handleSubmit} className="auth-form" noValidate>
        <label className="form-field">Email address
          <span className="auth-input-wrap"><Mail size={17} /><input type="email" autoComplete="email" required value={email} onChange={e => { setEmail(e.target.value); setFieldErrors(v => ({...v, email: ""})); }} placeholder="you@example.com" aria-invalid={Boolean(fieldErrors.email)} /></span>
          {fieldErrors.email && <small className="field-error" role="alert">{fieldErrors.email}</small>}
        </label>
        <label className="form-field">Password
          <span className="auth-input-wrap"><LockKeyhole size={17} /><input type="password" autoComplete="current-password" required value={password} onChange={e => { setPassword(e.target.value); setFieldErrors(v => ({...v, password: ""})); }} placeholder="Enter your password" aria-invalid={Boolean(fieldErrors.password)} /></span>
          {fieldErrors.password && <small className="field-error" role="alert">{fieldErrors.password}</small>}
        </label>
        {error && <p className="error-message" role="alert">{error}</p>}
        <button className="button button-primary auth-submit" type="submit" disabled={busy}>{busy ? "Signing in…" : "Sign in"}</button>
      </form>
      <p className="auth-switch">New here? <Link to="/register">Create an account</Link></p>
      <p className="auth-footnote">Learning project · JWT access-token authentication</p>
    </section></main>
  );
}
