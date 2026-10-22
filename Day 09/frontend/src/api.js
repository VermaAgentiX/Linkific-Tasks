const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    let message = `Request failed (${response.status})`;

    try {
      const data = await response.json();
      message = data.detail || message;
    } catch {
      // Keep the original status message if the response is not JSON.
    }

    throw new Error(message);
  }

  return response.json();
}

export const studentApi = {
  getAll(search = "") {
    const query = search ? `?q=${encodeURIComponent(search)}` : "";
    return request(`/students${query}`);
  },

  getById(id) {
    return request(`/students/${id}`);
  },

  getStats() {
    return request("/stats");
  },

  create(student) {
    return request("/students", {
      method: "POST",
      body: JSON.stringify(student),
    });
  },

  update(id, student) {
    return request(`/students/${id}`, {
      method: "PUT",
      body: JSON.stringify(student),
    });
  },

  remove(id) {
    return request(`/students/${id}`, {
      method: "DELETE",
    });
  },
};
