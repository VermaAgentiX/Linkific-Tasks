# Student Record Manager

> **Day 21 — Weekly Assessment: Production Readiness Review**  
> This README documents the project and the Day 21 review scope. Mark review items complete only after verifying them in the current checkout.

A full-stack student management application built with **React**, **FastAPI**, and **PostgreSQL**. It supports JWT authentication, role-based access control, and user-scoped student record management.

## Features

- User registration and JWT-based login
- Protected routes and authenticated API requests
- Role-based access control for administrator features
- Create, read, update, and delete student records
- Search student records
- Student details view
- Input validation and structured API errors
- PostgreSQL persistence through SQLAlchemy
- Admin user listing and dashboard statistics

## Screenshots

Add current screenshots of your running application to `docs/screenshots/` and update the paths below.

| Screen | Preview |
|---|---|
| Login | ![Login](docs/screenshots/login.png) |
| Dashboard | ![Dashboard](docs/screenshots/dashboard.png) |
| Student list | ![Student list](docs/screenshots/students.png) |
| Student form | ![Student form](docs/screenshots/student-form.png) |
| Admin page | ![Admin page](docs/screenshots/admin.png) |

> Screenshot placeholders are included for documentation structure. Capture screenshots from your own running application and save them using the filenames above.

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript, Tailwind CSS |
| Backend | Python, FastAPI, Pydantic |
| Database | PostgreSQL, SQLAlchemy |
| Authentication | JWT, password hashing |
| API testing | Postman |
| Development | VS Code |

## Project Structure

```text
Student-Record-Manager/
├── backend/
│   ├── main.py                 # FastAPI routes, authentication, authorization
│   ├── database.py             # Database engine, session, Base
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic request/response schemas
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Environment variable template
│   └── RESTORE_INSTRUCTIONS.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Routes and app composition
│   │   ├── main.jsx            # React entry point
│   │   ├── api.js              # API client
│   │   ├── styles.css           # Global styles
│   │   ├── auth/               # Auth context and route guards
│   │   ├── layouts/             # Protected application layout
│   │   ├── components/          # Reusable UI components
│   │   ├── pages/               # Route-level screens
│   │   └── utils/                # Shared validation utilities
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── docs/
│   ├── API.md                   # API reference
│   └── screenshots/              # Application screenshots
└── README.md
```

## Prerequisites

- Python 3.10 or newer
- Node.js 18 or newer and npm
- PostgreSQL (recommended: PostgreSQL 16+)
- Git

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Student-Record-Manager
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository's actual clone URL.

### 2. Configure PostgreSQL

Create a database and a database user, or use an existing PostgreSQL account:

```sql
CREATE DATABASE student_record_manager;
```

### 3. Configure backend environment

```bash
cd backend
```

Copy `.env.example` to `.env` and configure the database URL, JWT secret, and administrator email(s). Do not commit `.env`.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_URL_ENCODED_PASSWORD@localhost:5432/student_record_manager
SECRET_KEY=replace_with_a_long_random_secret
ADMIN_EMAILS=admin@example.com
```

If the database password contains URL-reserved characters, URL-encode them in `DATABASE_URL`.

Install dependencies and run the API:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

### 4. Configure and run frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Vite will print the local frontend URL (typically `http://localhost:5173`).

If the frontend API base URL is configurable in your environment, set it to `http://127.0.0.1:8000` as documented in `frontend/.env.example`.

## API Documentation

Interactive OpenAPI documentation is available while the backend is running:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

See [`docs/API.md`](docs/API.md) for endpoint details and sample requests.

## Authentication and Roles

1. Register or log in to receive an access token.
2. For protected endpoints, send `Authorization: Bearer <access_token>`.
3. Administrator access is configured through `ADMIN_EMAILS` in the backend environment.
4. Student records are scoped to their owner; users cannot read or modify another user's records.

## Testing

- Use Swagger UI or Postman to test API endpoints.
- Test valid and invalid registration/login payloads.
- Test student CRUD and search.
- Test missing/invalid tokens and role restrictions.
- Verify database changes with PostgreSQL queries.
- Run frontend build:

```bash
cd frontend
npm run build
```

## Day 21 — Weekly Assessment: Production Readiness Review

The weekly assessment reviews the Student Record Manager for correctness, maintainability, security, and deployment readiness.

### Review scope

- [ ] Verify registration, login, token handling, logout, and protected-route behavior.
- [ ] Review role-based access control and ownership checks for student records.
- [ ] Inspect database models, relationships, constraints, and persistence behavior.
- [ ] Explain the React component/page/layout structure and state flow.
- [ ] Trace frontend-to-backend communication, request handling, and API error display.
- [ ] Exercise input validation, malformed requests, and expected error responses.
- [ ] Run API checks and frontend build; record actual outcomes.
- [ ] Review responsive UI behavior and fix confirmed defects.
- [ ] Check folder organization, naming, duplication, and code readability.
- [ ] Review README, API documentation, setup instructions, and screenshots.
- [ ] Review deployment configuration, environment variables, secrets, and production risks.
- [ ] Update Git history with meaningful, focused commits.

### Verification record

Record commands, results, and any remaining issues here before marking the assessment complete.

| Check | Command / method | Result |
|---|---|---|
| Backend tests / API checks | Swagger UI or test suite | Not verified |
| Frontend production build | `cd frontend && npm run build` | Not verified |
| Authentication and authorization | Register/login and protected endpoints | Not verified |
| Student CRUD and validation | API/UI scenarios | Not verified |
| Responsive UI | Browser viewport checks | Not verified |
| Deployment readiness | Environment/configuration review | Not verified |

### Architecture review topics

- **Authentication flow:** registration/login → password verification → JWT issuance → bearer-token request → token validation and authorization.
- **Database structure:** SQLAlchemy models and PostgreSQL persistence; consult `backend/models.py` and `backend/database.py` for the implementation.
- **React architecture:** route-level pages, reusable components, layouts, auth context, and API client under `frontend/src/`.
- **Frontend/backend communication:** API client sends requests to FastAPI; the backend validates input, applies authorization, interacts with PostgreSQL, and returns structured responses.

These are review topics; confirm details against the current source before presenting them as verified implementation behavior.

### DSA revision

- **Longest Substring Without Repeating Characters** — use a sliding window and a set/map to track characters.
- **Merge Intervals** — sort intervals by start, then merge overlapping ranges.

## Future Improvements

- Add automated backend tests with pytest and FastAPI TestClient.
- Add frontend unit and component tests.
- Add pagination and sorting for student lists.
- Add Docker Compose for one-command local setup.
- Add CI workflow for linting, tests, and build checks.
- Add audit logs and more granular permissions.
- Improve deployment configuration and observability.

## Contributing

1. Create a feature branch.
2. Keep components and functions focused and reusable.
3. Add or update tests for behavior changes.
4. Update documentation when API or setup steps change.
5. Open a pull request describing the change and verification performed.

## Security Notes

- Never commit `.env`, database credentials, or production secrets.
- Use a strong, unique JWT secret.
- Use HTTPS in production.
- Keep dependencies updated.
- Do not expose internal exception details in API responses.

## License

Add your chosen license before publishing the repository publicly.
