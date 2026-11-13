# FinanceFlow AI — Day 24: Core Backend Development

Runnable React + FastAPI starter for the FinanceFlow AI project.

## Day 24 deliverables
- PostgreSQL connection with SQLite fallback
- SQLAlchemy models: categories, transactions, customers, suppliers, budgets
- CRUD APIs with Pydantic request validation
- Modular FastAPI structure (models, schemas, services, routes, config, database)
- React frontend connected to transaction/category APIs
- Postman collection
- Docker Compose for PostgreSQL

> This is a learning/MVP foundation. Authentication, workspace isolation, audit logging, immutable customer/supplier ledgers, Alembic migrations and production deployment are future tasks. Do not expose this unauthenticated API publicly or use it with real financial data.

## Run database
From the project root:
```bash
docker compose up -d db
```
Postgres defaults: `localhost:5432`, database/user `financeflow`, password `financeflow_dev`.

## Run backend (Windows PowerShell)
```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```
macOS/Linux: use `source .venv/bin/activate` and `cp .env.example .env`.

API docs: http://127.0.0.1:8000/docs  
Health: http://127.0.0.1:8000/health

### SQLite without Docker
Set `DATABASE_URL=sqlite:///./financeflow.db` in `backend/.env`.

## Run frontend
```bash
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```
Open the Vite URL, normally http://localhost:5173.

## Postman
Import `postman/FinanceFlow_AI_Day24.postman_collection.json`. Set `baseUrl` to `http://localhost:8000`. Start with Health Check, then create category/transaction and test GET, PUT, DELETE.

## Endpoints
| Resource | Endpoints |
|---|---|
| Categories | GET/POST `/api/v1/categories`; GET/PUT/DELETE `/api/v1/categories/{id}` |
| Transactions | GET/POST `/api/v1/transactions`; GET/PUT/DELETE `/api/v1/transactions/{id}` |
| Customers | GET/POST `/api/v1/customers`; GET/PUT/DELETE `/api/v1/customers/{id}` |
| Suppliers | GET/POST `/api/v1/suppliers`; GET/PUT/DELETE `/api/v1/suppliers/{id}` |
| Budgets | GET/POST `/api/v1/budgets`; GET/PUT/DELETE `/api/v1/budgets/{id}` |

List endpoints support `skip` and `limit`. Transactions also support `type` and `search` query filters.

Money is stored as `NUMERIC` and validated with `Decimal`, not float. Amounts must be positive. Dates use ISO `YYYY-MM-DD`.

## Suggested Day 24 verification
1. Start PostgreSQL and API.
2. Open `/docs`; confirm all CRUD routes are listed.
3. Import the Postman collection and run Health Check.
4. Create a category, then create a transaction.
5. Verify GET list/detail, PUT update and DELETE.
6. Send invalid payloads (negative amount, invalid type, short title) and confirm HTTP 422.
7. Commit the project and collection to GitHub.
