import { useEffect, useState } from "react";
import { ShieldCheck, Users, AlertCircle } from "lucide-react";
import { adminApi } from "../api.js";

export default function AdminPage() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    adminApi.getUsers().then(setUsers).catch(err => setError(err.message || "Unable to load accounts.")).finally(() => setLoading(false));
  }, []);
  return (
    <section className="page-section">
      <div className="page-heading">
        <div><p className="eyebrow">ACCESS CONTROL</p><h1><ShieldCheck size={25} style={{verticalAlign:"middle",marginRight:8}} />Admin Panel</h1><p>Only administrators can view registered accounts.</p></div>
      </div>
      <div className="panel-card">
        <h2><Users size={19} style={{verticalAlign:"middle",marginRight:8}} />Registered accounts</h2>
        {loading && <p>Loading accounts…</p>}
        {error && <p className="error-message" role="alert"><AlertCircle size={16}/> {error}</p>}
        {!loading && !error && <div className="table-wrap"><table className="data-table">
          <thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Role</th></tr></thead>
          <tbody>{users.map(u=><tr key={u.id}><td>{u.id}</td><td>{u.name}</td><td>{u.email}</td><td><span className={`role-pill role-${u.role}`}>{u.role}</span></td></tr>)}
          {users.length===0 && <tr><td colSpan="4">No accounts found.</td></tr>}</tbody>
        </table></div>}
      </div>
    </section>
  );
}
