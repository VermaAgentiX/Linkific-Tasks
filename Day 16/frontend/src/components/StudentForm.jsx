import { useEffect, useState } from "react";
import { Save } from "lucide-react";
import { validateStudent } from "../utils/validation.js";

const emptyForm = { name: "", age: "", course: "", email: "" };

export default function StudentForm({ initialStudent = null, onSave, buttonLabel = "Save student" }) {
  const [form, setForm] = useState(emptyForm);
  const [errors, setErrors] = useState({});
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    setForm(initialStudent ? {
      name: initialStudent.name || "",
      age: String(initialStudent.age ?? ""),
      course: initialStudent.course || "",
      email: initialStudent.email || "",
    } : emptyForm);
    setErrors({});
    setError("");
  }, [initialStudent]);

  function handleChange(event) {
    const { name, value } = event.target;
    setForm(current => ({ ...current, [name]: value }));
    setErrors(current => ({ ...current, [name]: "" }));
    setError("");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const nextErrors = validateStudent(form);
    setErrors(nextErrors);
    setError("");
    if (Object.keys(nextErrors).length) {
      document.querySelector(`[name="${Object.keys(nextErrors)[0]}"]`)?.focus();
      return;
    }

    setSaving(true);
    try {
      await onSave({
        name: form.name.trim(),
        age: Number(form.age),
        course: form.course.trim(),
        email: form.email.trim().toLowerCase(),
      });
    } catch (saveError) {
      if (saveError.fieldErrors) setErrors(current => ({ ...current, ...saveError.fieldErrors }));
      setError(saveError.message || "Unable to save this student. Please try again.");
    } finally {
      setSaving(false);
    }
  }

  const field = (name, label, props = {}) => (
    <label className="form-field">
      {label}
      <input
        name={name}
        value={form[name]}
        onChange={handleChange}
        aria-invalid={Boolean(errors[name])}
        aria-describedby={errors[name] ? `${name}-error` : undefined}
        {...props}
      />
      {errors[name] && <small className="field-error" id={`${name}-error`} role="alert">{errors[name]}</small>}
    </label>
  );

  return (
    <form className="panel form-panel" onSubmit={handleSubmit} noValidate>
      <div className="panel-heading">
        <h2>{initialStudent ? "Edit student details" : "Student details"}</h2>
        <p>Enter the student's information below.</p>
      </div>
      <div className="form-grid">
        {field("name", "Full name", { placeholder: "e.g. Aditi Sharma", minLength: 2, maxLength: 80, autoComplete: "name" })}
        {field("age", "Age", { type: "number", placeholder: "e.g. 21", min: 1, max: 120, step: 1 })}
        {field("course", "Course", { placeholder: "e.g. Computer Science", minLength: 2, maxLength: 100 })}
        {field("email", "Email address", { type: "email", placeholder: "student@example.com", maxLength: 254, autoComplete: "email" })}
      </div>
      {error && <p className="error-message" role="alert">{error}</p>}
      <button className="button button-primary" type="submit" disabled={saving}>
        <Save size={17} /> {saving ? "Saving..." : buttonLabel}
      </button>
    </form>
  );
}
