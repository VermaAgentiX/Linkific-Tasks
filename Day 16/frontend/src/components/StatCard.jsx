export default function StatCard({ icon: Icon, label, value, tone = "blue" }) {
  return (
    <article className="stat-card">
      <span className={`stat-icon stat-icon-${tone}`}>
        <Icon size={21} />
      </span>
      <p>{label}</p>
      <strong>{value}</strong>
    </article>
  );
}
