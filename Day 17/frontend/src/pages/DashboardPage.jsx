import { ArrowRight, GraduationCap, Users, UserRound } from "lucide-react";
import { Link } from "react-router-dom";

import StatCard from "../components/StatCard.jsx";

export default function DashboardPage({ students, stats, loading }) {
  const recentStudents = [...students].slice(-5).reverse();

  return (
    <>
      <section className="welcome-banner">
        <p className="eyebrow">STUDENT MANAGEMENT PORTAL</p>
        <h1>A simpler way to manage student records.</h1>
        <p className="welcome-description">
          Create student records, find information quickly, and manage updates
          from one organized workspace.
        </p>

        <div className="banner-actions">
          <Link className="button button-white" to="/students/new">
            Add a student
          </Link>
          <Link className="button button-outline" to="/students">
            View all students <ArrowRight size={16} />
          </Link>
        </div>
      </section>

      <section className="stats-grid" aria-label="Student statistics">
        <StatCard
          icon={Users}
          label="Total students"
          value={stats?.total_students ?? "—"}
          tone="blue"
        />
        <StatCard
          icon={GraduationCap}
          label="Courses represented"
          value={stats?.total_courses ?? "—"}
          tone="purple"
        />
        <StatCard
          icon={UserRound}
          label="Average age"
          value={stats ? stats.average_age : "—"}
          tone="green"
        />
      </section>

      <section className="panel recent-panel">
        <div className="panel-toolbar">
          <div className="panel-heading">
            <h2>Recently added students</h2>
            <p>The latest records returned by the API.</p>
          </div>
          <Link className="text-link" to="/students">
            View all <ArrowRight size={15} />
          </Link>
        </div>

        {loading ? (
          <p className="table-message">Loading dashboard data...</p>
        ) : recentStudents.length ? (
          <div className="recent-list">
            {recentStudents.map((student) => (
              <div className="recent-student" key={student.id}>
                <div className="student-avatar">
                  {student.name
                    .split(" ")
                    .map((part) => part[0])
                    .slice(0, 2)
                    .join("")
                    .toUpperCase()}
                </div>

                <div className="recent-student-info">
                  <strong>{student.name}</strong>
                  <span>{student.course} · {student.email}</span>
                </div>

                <Link to={`/students/${student.id}`} className="text-link">
                  Details
                </Link>
              </div>
            ))}
          </div>
        ) : (
          <div className="empty-state">
            <Users size={28} />
            <strong>No student records yet</strong>
            <p>Add a student to see live data on your dashboard.</p>
          </div>
        )}
      </section>
    </>
  );
}
