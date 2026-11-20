# FinanceFlow AI — Day 27

**Testing, Documentation & Deployment Preparation**  
**Stack:** React + Vite + Axios · FastAPI · Pydantic v2 · SQLAlchemy 2 · SQLite / PostgreSQL

FinanceFlow AI is a personal and small-business finance management project. The application brings transaction, budget, category, customer, and supplier workflows into one dashboard. This Day 27 version continues the Day 26 codebase and adds API-level tests, clearer documentation, deployment containers, a Docker Compose environment, and a CI workflow.

> **Project status:** This is a learning and deployment-preparation build. Backend tests were run in the build environment. The frontend production build and a live deployment were not verified here. Authentication, workspace-level authorization, and production database migrations are still required before handling real financial data.

## What's included in Day 27

### Quality and testing

- Existing schema validation tests retained.
- API tests added for health checks, category CRUD, transaction creation/search/filtering, invalid input, and missing records.
- Isolated in-memory SQLite database used by API tests so test records do not touch the local development database.
- GitHub Actions workflow added for backend tests and frontend build checks.
- Corrected the frontend entry file's stray leading character and fixed the Nginx API proxy path.
- Corrected the backend dependency file so each requirement is on its own line.

### Documentation

- Expanded this README with setup, architecture, API, testing, deployment, and known limitations.
- Added `docs/API_REFERENCE.md` for endpoint patterns, filters, sample payloads, and error formats.
- Added `docs/ARCHITECTURE.md` for the request lifecycle and frontend navigation design.
- Added `docs/DEPLOYMENT.md` for container deployment preparation and a production-readiness checklist.
- Added `docs/SCREENSHOTS.md` with a checklist for capturing genuine application screenshots.

### Deployment preparation

- Backend Dockerfile using Python 3.12.
- Frontend multi-stage Dockerfile using Node and Nginx.
- Nginx configuration serving the React build and proxying API requests.
- Docker Compose services for PostgreSQL, FastAPI, and the frontend.
- `.env.example`, `.gitignore`, and `.dockerignore` files.

## Project structure

```text
FinanceFlow_AI_Day27/
├── .github/workflows/ci.yml
├── backend/
│   ├── app/
│   │   ├── api/routes/       # HTTP endpoints
│   │   ├── core/             # Settings and database session
│   │   ├── models/           # SQLAlchemy entities
│   │   ├── schemas/          # Pydantic request/response schemas
│   │   ├── services/         # Reusable database operations
│   │   └── main.py           # FastAPI application
│   ├── tests/                # Schema and API tests
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main app shell and page components
│   │   ├── api.js            # Shared Axios client and resource methods
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── Dockerfile
│   └── nginx.conf
├── docs/
│   ├── API_REFERENCE.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   └── SCREENSHOTS.md
├── screenshots/              # Add real captures after running the app
├── postman/
├── docker-compose.yml
└── README.md
```

## Run locally on Windows

### 1. Backend

Open CMD in the `backend` directory:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload
```

SQLite is used by default. The database file is created locally in the backend directory. Docker is not required for this development mode.

- API root: http://localhost:8000/
- Health: http://localhost:8000/api/v1/health
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

### 2. Frontend

Open a second CMD window in the `frontend` directory:

```cmd
copy .env.example .env
npm install
npm run dev
```

Open http://localhost:5173. The local `.env` should contain:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

Restart the Vite server after changing environment variables.

## Run tests

From the `backend` directory with the virtual environment active:

```cmd
python -m pytest -q
```

The Day 27 backend test suite contains **9 tests** across schema and API behavior. The API tests use a temporary in-memory SQLite database.

## Build the frontend

From the `frontend` directory:

```cmd
npm install
npm run build
```

Vite writes the production bundle to `frontend/dist/`. This build command should be run locally and in CI before submitting a release.

## Docker Compose deployment rehearsal

Install Docker Desktop, then run these commands from the project root:

```cmd
copy .env.example .env
```

Edit `.env` and replace `POSTGRES_PASSWORD` with a strong local password. Then:

```cmd
docker compose up --build
```

Open http://localhost:8080. Nginx serves the built frontend and forwards `/api/` requests to FastAPI. PostgreSQL data is stored in the named Docker volume `financeflow_data`.

Stop the services:

```cmd
docker compose down
```

To delete the local database volume as well (destructive):

```cmd
docker compose down -v
```

See [Deployment Preparation](docs/DEPLOYMENT.md) before using any hosted environment.

## API overview

All versioned endpoints use `/api/v1`.

| Resource | Supported operations |
|---|---|
| `/categories` | List, create, retrieve, update, delete |
| `/transactions` | List, create, retrieve, update, delete; search and filters |
| `/customers` | List, create, retrieve, update, delete |
| `/suppliers` | List, create, retrieve, update, delete |
| `/budgets` | List, create, retrieve, update, delete |

Transaction list filters include `q`, `type`, `start_date`, `end_date`, `sort`, `skip`, and `limit`. Refer to [API Reference](docs/API_REFERENCE.md) or `/docs` for full details.

## Architecture at a glance

1. React page components collect user input and display data.
2. The shared Axios client sends requests to FastAPI.
3. FastAPI validates requests with Pydantic schemas.
4. Route handlers use SQLAlchemy sessions and CRUD services.
5. SQLAlchemy reads and writes SQLite locally or PostgreSQL in the Docker setup.
6. Structured API responses and errors are reflected in the frontend.

The current UI is a single-page application with page selection managed in `App.jsx`; it does not yet use a dedicated URL router. See [Architecture](docs/ARCHITECTURE.md).

## Screenshots

The `screenshots/` directory is intentionally supplied for genuine captures from your local run. Follow [Screenshot Evidence Guide](docs/SCREENSHOTS.md). No fabricated application screenshots are included.

## Known limitations and next engineering steps

- Authentication and server-side authorization are not implemented.
- The workspace selector is a UI-level concept only; it does not isolate user data.
- `Base.metadata.create_all()` is used for convenient local setup. Add Alembic migrations before deploying schema changes.
- The AI Insights page is deterministic/demo content, not a connected LLM agent.
- Customer and supplier balances are not yet ledger-derived.
- Add integration tests for every resource and regression tests for the full frontend workflows.
- Configure TLS, backups, monitoring, rate limits, and managed secrets before public deployment.

Do not use real customer, supplier, or bank data in this training build.

## Day 27 GitHub submission

From the project root:

```cmd
git status
git add .
git commit -m "Day 27: add tests, API docs and deployment preparation"
git push
```

GitHub is not updated automatically by generating this archive. Run the commands above in your own repository after reviewing the changes.
