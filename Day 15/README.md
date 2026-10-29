# Student Record Manager — Day 15: Authentication & Authorization

A React + FastAPI student-record application enhanced with JWT authentication, logout, protected routes, protected APIs, and basic Admin/User role-based access control (RBAC).

## Day 15 requirements covered

- Login and registration with JWT access tokens.
- Logout that clears the browser's stored token and in-memory API token.
- React protected routes for authenticated pages.
- Backend JWT verification for student APIs.
- Basic `admin` and `user` roles.
- Admin-only `/admin` frontend route and `GET /admin/users` API.
- `401 Unauthorized` for missing/invalid/expired tokens.
- `403 Forbidden` for authenticated users without the required role.
- Argon2 password hashing.
- Account-scoped student CRUD and search.
- PostgreSQL through SQLAlchemy, with SQLite fallback if configured.

## Project structure

```text
Student-Record-Manager/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── auth/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api.js
│   │   └── App.jsx
│   ├── package.json
│   └── ...
└── README.md
```

## 1. Configure PostgreSQL and environment

Create the database if you have not already created it:

```sql
CREATE DATABASE student_record_manager;
```

Copy `backend/.env.example` to `backend/.env`, then set your local credentials:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:URL_ENCODED_PASSWORD@localhost:5432/student_record_manager
JWT_SECRET_KEY=PUT_A_UNIQUE_RANDOM_SECRET_HERE
JWT_EXPIRE_MINUTES=60
ADMIN_EMAILS=admin@example.com
```

Generate a strong secret with Python:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Use the generated value for `JWT_SECRET_KEY`. URL-encode reserved characters in the database password. Never commit `.env` or share its contents.

### Set up an administrator

The public registration endpoint does not accept a role, so users cannot grant themselves admin access.

1. Set `ADMIN_EMAILS` to the email address that should be the administrator before registering that account.
2. Register using that exact email address. The API assigns the `admin` role.
3. If the account already exists, add its email to `ADMIN_EMAILS` and restart FastAPI; the startup step promotes that matching account.
4. Sign out and sign in again to receive a token reflecting the account's role, then open `/admin`.

For multiple admins, separate emails with commas. Keep this setting private and controlled by the developer/operator.

## 2. Run the backend

From a terminal in `backend/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
```

Check:

- API docs: http://127.0.0.1:8000/docs
- Database-aware health check: http://127.0.0.1:8000/health

The health endpoint should return `{"status":"ok","database":"connected"}` when the configured database is reachable.

## 3. Run the frontend

Open another terminal in `frontend/`:

```powershell
npm install
npm run dev
```

Open the local URL Vite prints (normally http://localhost:5173).

## Roles and authorization

| Capability | User | Admin |
|---|---:|---:|
| Register/login | Yes | Yes |
| View and manage own student records | Yes | Yes |
| Access `/admin` | No | Yes |
| Call `GET /admin/users` | No (403) | Yes |

Backend role checks are the security boundary. Hiding the Admin navigation link is only a user-interface convenience; requests are independently authorized by FastAPI.

## API endpoints

| Method | Endpoint | Access |
|---|---|---|
| POST | `/auth/register` | Public |
| POST | `/auth/login` | Public |
| POST | `/auth/logout` | Valid JWT |
| GET | `/auth/me` | Valid JWT |
| GET | `/students` | Valid JWT; own records only |
| GET | `/students/{student_id}` | Valid JWT; own record only |
| POST | `/students` | Valid JWT |
| PUT | `/students/{student_id}` | Valid JWT; own record only |
| DELETE | `/students/{student_id}` | Valid JWT; own record only |
| GET | `/stats` | Valid JWT; own records only |
| GET | `/admin/users` | Admin only |
| GET | `/health` | Database connectivity check |

## Test checklist

- [ ] Register a regular user and confirm response role is `user`.
- [ ] Log in and confirm a token is returned.
- [ ] Open a protected page while signed out; it should redirect to `/login`.
- [ ] Call a protected API without a token; it should return `401`.
- [ ] Call `GET /admin/users` as a regular user; it should return `403`.
- [ ] Configure an admin email, register/promote that account, and sign in again.
- [ ] Confirm the admin sees the Admin navigation link and can open `/admin`.
- [ ] Confirm the admin endpoint returns user list without password hashes.
- [ ] Click Sign out and confirm the app returns to login/protected pages are inaccessible.
- [ ] Confirm each user can access only their own student records.
- [ ] Verify expired/invalid tokens are rejected.
- [ ] Verify student CRUD and search still work after database integration.

## Important security note about logout

JWT access tokens are stateless. The frontend calls `/auth/logout` and then deletes the token from localStorage and memory. This logs out the current browser, but does not revoke a copied token on the server. The token remains usable until it expires. For production, consider short access-token lifetimes and a refresh-token rotation/revocation design.

## Database migration note

SQLAlchemy creates missing tables on startup. This project also includes a small additive migration for the `role` column on an existing `users` table. It is a learning-project migration, not a replacement for Alembic in production. Back up important database data before running schema changes.

## Day 15 learning outcomes

- Authentication verifies identity; authorization decides what an authenticated user may do.
- JWTs carry signed claims and are checked by backend dependencies.
- React route guards improve navigation flow but do not replace backend API authorization.
- Role-based access control restricts administrator functionality.
- Passwords should be hashed with Argon2 rather than stored as plaintext.
- Logout for stateless JWTs requires clearing the client token; server-side revocation needs an additional design.

## Author

Abhishek Verma — Linkific Internship, Day 15
