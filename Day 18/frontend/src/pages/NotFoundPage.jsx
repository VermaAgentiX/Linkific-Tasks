import { ArrowLeft } from "lucide-react";
import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <section className="panel not-found">
      <p className="eyebrow-dark">404 ERROR</p>
      <h1>Page not found</h1>
      <p>This page does not exist or may have moved.</p>
      <Link to="/" className="button button-primary">
        <ArrowLeft size={16} /> Back to dashboard
      </Link>
    </section>
  );
}
