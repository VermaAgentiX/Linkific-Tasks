import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { GraduationCap, LockKeyhole, Mail, UserRound } from "lucide-react";
import { useAuth } from "../auth/AuthContext.jsx";
import { validateRegistration } from "../utils/validation.js";

export default function RegisterPage() {
  const { user, signUp } = useAuth();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [fieldErrors, setFieldErrors] = useState({});
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();
  if (user) return <Navigate to="/" replace />;

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    const nextErrors = validateRegistration({ name, email, password });
    setFieldErrors(nextErrors);
    if (Object.keys(nextErrors).length) return;
    setBusy(true);
    try {
      await signUp(name.trim(), email.trim().toLowerCase(), password);
      navigate("/", { replace: true });
    } catch (err) {
      setFieldErrors(err.fieldErrors || {});
      setError(err.message || "Unable to create account. Please try again.");
    } finally { setBusy(false); }
  }

  return (
    <main className="auth-page"><section className="auth-card">
      <div className="auth-brand-icon"><GraduationCap size={30} /></div>
      <p className="auth-eyebrow">STUDENT RECORD MANAGER</p><h1>Create your account</h1>
      <p className="auth-subtitle">Register to access the student workspace.</p>
      <form onSubmit={handleSubmit} className="auth-form" noValidate>
        <label className="form-field">Full name
          <span className="auth-input-wrap"><UserRound size={17} /><input type="text" autoComplete="name" minLength="2" maxLength="80" required value={name} onChange={e => { setName(e.target.value); setFieldErrors(v => ({...v, name: ""})); }} placeholder="Your name" aria-invalid={Boolean(fieldErrors.name)} /></span>
          {fieldErrors.name && <small className="field-error" role="alert">{fieldErrors.name}</small>}
        </label>
        <label className="form-field">Email address
          <span className="auth-input-wrap"><Mail size={17} /><input type="email" autoComplete="email" required value={email} onChange={e => { setEmail(e.target.value); setFieldErrors(v => ({...v, email: ""})); }} placeholder="you@example.com" aria-invalid={Boolean(fieldErrors.email)} /></span>
          {fieldErrors.email && <small className="field-error" role="alert">{fieldErrors.email}</small>}
        </label>
        <label className="form-field">Password
          <span className="auth-input-wrap"><LockKeyhole size={17} /><input type="password" autoComplete="new-password" minLength="8" maxLength="128" required value={password} onChange={e => { setPassword(e.target.value); setFieldErrors(v => ({...v, password: ""})); }} placeholder="At least 8 characters" aria-invalid={Boolean(fieldErrors.password)} /></span>
          {fieldErrors.password && <small className="field-error" role="alert">{fieldErrors.password}</small>}
        </label>
        {error && <p className="error-message" role="alert">{error}</p>}
        <button className="button button-primary auth-submit" type="submit" disabled={busy}>{busy ? "Creating account…" : "Create account"}</button>
      </form>
      <p className="auth-switch">Already registered? <Link to="/login">Sign in</Link></p>
      <p className="auth-footnote">Passwords are hashed on the backend, not stored as plain text.</p>
    </section></main>
  );
}
