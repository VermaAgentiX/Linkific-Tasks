# FinanceFlow AI — Day 25 Backend (fixed)

This backend replaces the Day 25 backend folder. It is compatible with the Day 25 React frontend and its Axios client.

## Important fix for the reported traceback

The schemas import `date` using an explicit alias:

```python
from datetime import date as Date
```

Date annotations use `Date` and the schema module uses postponed annotation evaluation. This avoids a collision between the `date` type and the `date` field name.

## Install and run (Windows CMD)

Open CMD in this `backend` directory:

```cmd
python -m venv .venv
.venv\Scripts\activate
copy .env.example .env
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Do not run `fastapi dev main.py` from inside `backend\app`. Run Uvicorn from the `backend` folder so `app.main` imports resolve consistently.

Open:
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/api/v1/health

## Database

Default configuration uses SQLite, so Docker is not required for local Day 25 testing. It creates `financeflow.db` in the backend working directory.

For PostgreSQL, set `DATABASE_URL` in `.env` to:

```env
DATABASE_URL=postgresql+psycopg://financeflow:financeflow_dev@localhost:5432/financeflow
```

Make sure PostgreSQL is running before starting FastAPI.

## Frontend connection

The React `.env` should contain:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

Restart Vite after editing `.env`.

## Available resources

- `/api/v1/categories`
- `/api/v1/transactions`
- `/api/v1/transactions/search?q=rent`
- `/api/v1/customers`
- `/api/v1/suppliers`
- `/api/v1/budgets`

Each resource supports GET list, POST create, GET by ID, PUT update, DELETE by ID.

## Notes

- Request validation uses Pydantic v2.
- Database operations use SQLAlchemy 2.x.
- Financial amounts use `Decimal` / SQL `NUMERIC(14,2)`.
- This is a learning project. Authentication, tenant isolation, a full accounting ledger and Alembic migrations are not included.
