const API_URL = (
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
).replace(/\/$/, "");

let accessToken = "";

export function setAccessToken(token) {
  accessToken = token || "";
}

async function request(path, options = {}) {
  let response;
  const headers = {
    ...(options.body ? { "Content-Type": "application/json" } : {}),
    ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
    ...options.headers,
  };

  try {
    response = await fetch(`${API_URL}${path}`, { ...options, headers });
  } catch (error) {
    if (error.name === "AbortError") throw error;
    throw new Error(
      `Cannot reach the API at ${API_URL}. Check that FastAPI is running and the URL is correct.`
    );
  }

  if (!response.ok) {
    let message = `Request failed with status ${response.status}`;
    let data = null;
    try { data = await response.json(); } catch { /* Response may not contain JSON. */ }
    if (typeof data?.detail === "string") message = data.detail;
    else if (Array.isArray(data?.detail)) message = data.detail.map(item => item.msg).join("; ");
    else if (typeof data?.message === "string") message = data.message;

    const fieldErrors = {};
    if (Array.isArray(data?.errors)) {
      data.errors.forEach(item => {
        if (item?.field && item?.message) fieldErrors[item.field] = item.message;
      });
    } else if (Array.isArray(data?.detail)) {
      data.detail.forEach(item => {
        const field = item?.loc?.filter(part => part !== "body").join(".");
        if (field) fieldErrors[field] = String(item.msg || "Invalid value").replace("Value error, ", "");
      });
    }

    if (response.status === 401) {
      localStorage.removeItem("sr_access_token");
      accessToken = "";
      window.dispatchEvent(new CustomEvent("auth:expired"));
    }
    const apiError = new Error(Object.keys(fieldErrors).length ? "Please correct the highlighted fields." : message);
    apiError.status = response.status;
    if (Object.keys(fieldErrors).length) apiError.fieldErrors = fieldErrors;
    throw apiError;
  }

  if (response.status === 204) return null;
  const contentType = response.headers.get("content-type") || "";
  if (!contentType.includes("application/json")) {
    throw new Error("The API returned an unexpected response format. Expected JSON.");
  }
  return response.json();
}

export const authApi = {
  register(data) {
    return request("/auth/register", { method: "POST", body: JSON.stringify(data) });
  },
  login(data) {
    return request("/auth/login", { method: "POST", body: JSON.stringify(data) });
  },
  me() {
    return request("/auth/me");
  },
  logout() {
    return request("/auth/logout", { method: "POST" });
  },
};

export const studentApi = {
  getAll(search = "") {
    const query = search.trim() ? `?q=${encodeURIComponent(search.trim())}` : "";
    return request(`/students${query}`);
  },
  getById(id) {
    return request(`/students/${encodeURIComponent(id)}`);
  },
  getStats() {
    return request("/stats");
  },
  create(student) {
    return request("/students", { method: "POST", body: JSON.stringify(student) });
  },
  update(id, student) {
    return request(`/students/${encodeURIComponent(id)}`, {
      method: "PUT",
      body: JSON.stringify(student),
    });
  },
  remove(id) {
    return request(`/students/${encodeURIComponent(id)}`, { method: "DELETE" });
  },
};

export const adminApi = {
  getUsers() {
    return request("/admin/users");
  },
};
