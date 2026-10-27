# Day 13 -  Student Record Manager [Added JWT for user registration and authentication] 

A full-stack student management application built with **React**, **React Router**, and **FastAPI**. Day 13 adds a learning implementation of **JWT authentication**, password hashing, account registration, login, and protected routes/API endpoints.

## Features

- **Authentication:** Register and log in with an email and password.
- **JWT access tokens:** FastAPI issues signed, expiring bearer tokens after successful authentication.
- **Password hashing:** Passwords are hashed with Argon2 using `pwdlib`; plaintext passwords are not stored.
- **Protected frontend routes:** The dashboard and student-management pages require a valid signed-in session.
- **Protected backend APIs:** Student CRUD and dashboard statistics endpoints require a valid `Authorization: Bearer <token>` header.
- **Account-specific records:** Student records and dashboard statistics are scoped to the authenticated account.
- **Student CRUD:** Create, view, update, search, and delete student records.
- **Dashboard:** Displays student statistics.
- **Request feedback:** Frontend API helper handles HTTP errors, connection failures, and expired/invalid tokens.
- **API documentation:** Interactive Swagger UI is available at `/docs`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, JavaScript, React Router, Vite |
| API client | Fetch API with bearer-token authorization |
| Backend | Python, FastAPI, Uvicorn |
| Authentication | JWT access tokens with PyJWT |
| Password security | Argon2 password hashing via `pwdlib` |
| Validation | Pydantic, email validation |
| Styling | CSS, Tailwind configuration |

## Project Structure

```text
Student-Record-Manager/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── auth/
│   │   │   ├── AuthContext.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── LoginPage.jsx
│   │   │   ├── RegisterPage.jsx
│   │   │   └── ...
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── .env.example
│   └── package.json
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js and npm
- Git (optional)

### 1. Configure the backend secret

Create a strong random secret. For example:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Set it as `JWT_SECRET_KEY` in your environment. Do not commit real secrets to GitHub.

**Windows PowerShell:**

```powershell
cd backend
$env:JWT_SECRET_KEY = "paste-a-long-random-secret-here"
$env:JWT_EXPIRE_MINUTES = "60"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

**macOS/Linux:**

```bash
cd backend
export JWT_SECRET_KEY="paste-a-long-random-secret-here"
export JWT_EXPIRE_MINUTES="60"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Backend URLs:

- API: `http://127.0.0.1:8000`
- Health check: `http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`

The backend contains a local-only fallback secret to make first-time experimentation easier. Always set `JWT_SECRET_KEY` explicitly, especially before sharing or deploying the app.

### 2. Start the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the URL shown by Vite, usually `http://localhost:5173`.

Optional frontend environment file at `frontend/.env`:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Restart Vite after changing environment variables. Never put backend secrets in variables prefixed with `VITE_`; those values are exposed to browser code.

## Authentication Flow

1. A new user opens `/register` and submits a name, email, and password.
2. FastAPI validates the input, hashes the password with Argon2, and stores the account in the demo user store.
3. The API returns a signed JWT access token and public user details.
4. The frontend keeps the token for the session and includes it in API requests as `Authorization: Bearer <token>`.
5. Protected routes check whether the frontend has a valid signed-in user. Protected API endpoints independently verify the JWT signature and expiry.
6. `/auth/me` validates the current token and returns the signed-in user's public details.
7. On sign-out, the frontend removes the token. Invalid or expired tokens cause the user to be signed out.

## Frontend Routes

| Route | Access | Purpose |
|---|---|---|
| `/login` | Public | Sign in |
| `/register` | Public | Create an account |
| `/` | Protected | Dashboard |
| `/students` | Protected | List and search own student records |
| `/students/new` | Protected | Create a student |
| `/students/:id` | Protected | View a student |
| `/students/:id/edit` | Protected | Edit a student |
| `/about` | Protected | Project information |

## API Reference

Base URL: `http://127.0.0.1:8000`

### Authentication endpoints

| Method | Endpoint | Auth required | Purpose |
|---|---|---|---|
| `POST` | `/auth/register` | No | Register an account and return a token |
| `POST` | `/auth/login` | No | Validate credentials and return a token |
| `GET` | `/auth/me` | Yes | Return current user details |
| `GET` | `/health` | No | Health check |

### Protected student endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/stats` | Current user's dashboard statistics |
| `GET` | `/students` | List current user's student records |
| `GET` | `/students?q=alex` | Search current user's records |
| `GET` | `/students/{student_id}` | Retrieve one owned record |
| `POST` | `/students` | Create a record |
| `PUT` | `/students/{student_id}` | Update an owned record |
| `DELETE` | `/students/{student_id}` | Delete an owned record |

### Example registration request

`POST /auth/register`

```json
{
  "name": "Alex Morgan",
  "email": "alex@example.com",
  "password": "Use-a-strong-password"
}
```

The response contains `access_token`, `token_type`, and public user details. The password hash is never returned.

### Example authenticated request

Include the token returned from login or registration:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

For example, use that header when calling `GET /students`.

## Testing Checklist

- [ ] Start FastAPI and open `/docs`.
- [ ] Register a new account at `/register`.
- [ ] Confirm the app opens the dashboard after registration.
- [ ] Refresh the page and confirm the session is restored if the token is valid.
- [ ] Sign out and confirm protected pages redirect to `/login`.
- [ ] Log in using the same account.
- [ ] Try an incorrect password and confirm an error is displayed.
- [ ] Call a protected endpoint in Swagger UI without a token and confirm it returns `401`.
- [ ] Call a protected endpoint with a valid bearer token and confirm it succeeds.
- [ ] Register a second account and confirm it cannot access the first account's student records.
- [ ] Check that expired/invalid tokens result in a sign-in prompt.
- [ ] Push the verified source and README to GitHub.

## Security Notes and Limitations

This is an internship learning project, not a production-ready identity system.

- **In-memory accounts and records:** Data is lost when the backend restarts. Use a database for persistence.
- **Browser token storage:** This demo stores the access token in `localStorage`, which is convenient for learning but can be exposed by successful cross-site scripting (XSS). Production applications should evaluate secure, `HttpOnly`, `Secure`, `SameSite` cookies or another well-reviewed token-storage design.
- **No refresh-token workflow or revocation:** Access tokens expire, but this demo does not implement refresh tokens or a token denylist.
- **Rate limiting:** Login and registration endpoints should be rate-limited in production.
- **HTTPS:** Production deployments must use HTTPS.
- **Secret management:** Set a strong, unique `JWT_SECRET_KEY` through the deployment environment. Never commit it.
- **Data isolation:** Student records are scoped to the authenticated user in this demo. More complex applications should enforce authorization consistently at the data-access layer.
- **Production review:** Add automated tests, persistent database storage, logging, monitoring, and security review before deploying publicly.

## Learning Outcomes

This project demonstrates authentication versus authorization, password hashing, JWT creation and validation, token expiry, bearer authorization headers, protected React routes, protected FastAPI endpoints, and account-scoped CRUD operations.

## License

Add a `LICENSE` file if you intend to distribute this project under a specific open-source license.
