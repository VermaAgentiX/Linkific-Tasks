import { createContext, useContext, useEffect, useState } from "react";
import { authApi, setAccessToken } from "../api.js";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const handleExpired = () => {
      localStorage.removeItem("sr_access_token");
      setAccessToken("");
      setUser(null);
    };
    window.addEventListener("auth:expired", handleExpired);

    const token = localStorage.getItem("sr_access_token");
    if (!token) {
      setReady(true);
      return () => window.removeEventListener("auth:expired", handleExpired);
    }

    setAccessToken(token);
    authApi.me()
      .then(setUser)
      .catch(() => {
        localStorage.removeItem("sr_access_token");
        setAccessToken("");
      })
      .finally(() => setReady(true));

    return () => window.removeEventListener("auth:expired", handleExpired);
  }, []);

  async function signIn(email, password) {
    const result = await authApi.login({ email, password });
    localStorage.setItem("sr_access_token", result.access_token);
    setAccessToken(result.access_token);
    setUser(result.user);
    return result.user;
  }

  async function signUp(name, email, password) {
    const result = await authApi.register({ name, email, password });
    localStorage.setItem("sr_access_token", result.access_token);
    setAccessToken(result.access_token);
    setUser(result.user);
    return result.user;
  }

  async function signOut() {
    try {
      await authApi.logout();
    } catch {
      // Always clear local credentials, even if the token expired or the API is offline.
    } finally {
      localStorage.removeItem("sr_access_token");
      setAccessToken("");
      setUser(null);
    }
  }

  return (
    <AuthContext.Provider value={{ user, ready, signIn, signUp, signOut }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const value = useContext(AuthContext);
  if (!value) throw new Error("useAuth must be used inside AuthProvider");
  return value;
}
