import { useEffect, useState } from "react";
import { Save } from "lucide-react";

const emptyForm = {
  name: "",
  age: "",
  course: "",
  email: "",
};

export default function StudentForm({
  initialStudent = null,
  onSave,
  buttonLabel = "Save student",
}) {
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (initialStudent) {
      setForm({
        name: initialStudent.name,
        age: String(initialStudent.age),
        course: initialStudent.course,
        email: initialStudent.email,
      });
    } else {
      setForm(emptyForm);
    }

    setError("");
  }, [initialStudent]);

  function handleChange(event) {
    const { name, value } = event.target;

    setForm((currentForm) => ({
      ...currentForm,
      [name]: value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");

    const studentData = {
      name: form.name.trim(),
      age: Number(form.age),
      course: form.course.trim(),
      email: form.email.trim(),
    };

    if (!studentData.name || !studentData.course || !studentData.email) {
      setError("Please complete all fields.");
      return;
    }

    if (!Number.isInteger(studentData.age) || studentData.age < 1 || studentData.age > 120) {
      setError("Enter an age between 1 and 120.");
      return;
    }

    setSaving(true);

    try {
      await onSave(studentData);
    } catch (saveError) {
      setError(saveError.message || "Unable to save this student.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <form className="panel form-panel" onSubmit={handleSubmit}>
      <div className="panel-heading">
        <h2>{initialStudent ? "Edit student details" : "Student details"}</h2>
        <p>Enter the student's information below.</p>
      </div>

      <div className="form-grid">
        <label className="form-field">
          Full name
          <input
            name="name"
            value={form.name}
            onChange={handleChange}
            placeholder="e.g. Aditi Sharma"
            minLength={2}
            maxLength={80}
            required
          />
        </label>

        <label className="form-field">
          Age
          <input
            name="age"
            type="number"
            value={form.age}
            onChange={handleChange}
            placeholder="e.g. 21"
            min={1}
            max={120}
            required
          />
        </label>

        <label className="form-field">
          Course
          <input
            name="course"
            value={form.course}
            onChange={handleChange}
            placeholder="e.g. Computer Science"
            minLength={2}
            maxLength={100}
            required
          />
        </label>

        <label className="form-field">
          Email address
          <input
            name="email"
            type="email"
            value={form.email}
            onChange={handleChange}
            placeholder="student@example.com"
            maxLength={120}
            required
          />
        </label>
      </div>

      {error && (
        <p className="error-message" role="alert">
          {error}
        </p>
      )}

      <button className="button button-primary" type="submit" disabled={saving}>
        <Save size={17} />
        {saving ? "Saving..." : buttonLabel}
      </button>
    </form>
  );
}
