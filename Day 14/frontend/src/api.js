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
    try {
      const data = await response.json();
      if (typeof data.detail === "string") message = data.detail;
      else if (Array.isArray(data.detail)) message = data.detail.map(item => item.msg).join("; ");
      else if (typeof data.message === "string") message = data.message;
    } catch {
      // Some responses do not include a JSON body.
    }

    const apiError = new Error(message);
    apiError.status = response.status;
    if (response.status === 401) {
      localStorage.removeItem("sr_access_token");
      accessToken = "";
      window.dispatchEvent(new CustomEvent("auth:expired"));
    }
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
