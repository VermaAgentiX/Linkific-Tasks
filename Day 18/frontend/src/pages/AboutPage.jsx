import { Code2, Database, Route, Workflow } from "lucide-react";

const learningTopics = [
  {
    icon: Route,
    title: "React Router",
    description:
      "Move between dashboard, student list, add, edit, and detail pages without a full browser reload.",
  },
  {
    icon: Workflow,
    title: "React Hooks",
    description:
      "Use useState for changing interface data and useEffect to load information from the API.",
  },
  {
    icon: Database,
    title: "FastAPI CRUD",
    description:
      "Validate requests and create, read, update, and delete student records through REST endpoints.",
  },
  {
    icon: Code2,
    title: "Reusable components",
    description:
      "Keep navigation, forms, tables, and summary cards in separate files for easier maintenance.",
  },
];

export default function AboutPage() {
  return (
    <>
      <div className="page-heading">
        <p className="eyebrow-dark">PROJECT INFORMATION</p>
        <h1>About this project</h1>
        <p>A full-stack learning project built for the Linkific internship.</p>
      </div>

      <div className="learning-grid">
        {learningTopics.map(({ icon: Icon, title, description }) => (
          <article className="panel learning-card" key={title}>
            <span className="learning-icon">
              <Icon size={21} />
            </span>
            <h2>{title}</h2>
            <p>{description}</p>
          </article>
        ))}
      </div>

      <section className="notice-box">
        <strong>Storage note</strong>
        <p>
          This version stores records in a Python list in memory. Records reset
          when the backend restarts. A database can be added in a future version.
        </p>
      </section>
    </>
  );
}
