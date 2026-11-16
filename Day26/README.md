# FinanceFlow AI — Day 26: Feature Completion & Optimization

Day 26 continues the Day 24–25 project using React + Vite + Axios, FastAPI, Pydantic v2, SQLAlchemy 2.x and SQLite by default (PostgreSQL supported).

## Day 26 improvements

- Responsive Overview, Transactions, Budgets, Analytics, Customers, Suppliers, Categories, AI Insights and Settings pages.
- Create, read, update and delete forms for transactions, budgets, categories, customers and suppliers.
- Dynamic dashboard totals, category spending, budget utilization and six-month cash-flow chart.
- Loading, empty, success, API connection and error states.
- Transaction search through the global search field.
- Transaction filters for income/expense and date range.
- Sorting by date, amount and title.
- Pagination (10 rows per page) and filtered CSV export.
- Backend query filtering, sorting and pagination parameters.
- SQL indexes for common transaction date/type/category queries.
- Shared Axios client and centralized database commit/error handling.
- Pydantic validation for amounts, names, dates, email and enum fields.
- Blank optional email values are normalized to null.
- Budget end date cannot precede start date.

## Structure

```text
FinanceFlow_AI_Day26/
├── backend/
│   ├── app/api/routes/crud_routes.py
│   ├── app/core/
│   ├── app/models/entities.py
│   ├── app/schemas/resources.py
│   ├── app/services/crud.py
│   ├── app/main.py
│   ├── tests/test_schemas.py
│   └── requirements.txt
├── frontend/src/
├── postman/
└── docker-compose.yml
```

## Run on Windows

### Backend — terminal 1

Open CMD inside `backend`:

```cmd
python -m venv .venv
.venv\Scripts\activate
copy .env.example .env
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

SQLite is the default; Docker is not required. The database file is created in the backend directory.

- Swagger: http://localhost:8000/docs
- Health: http://localhost:8000/api/v1/health

### Frontend — terminal 2

Open CMD inside `frontend`:

```cmd
copy .env.example .env
npm install
npm run dev
```

Open http://localhost:5173. The frontend `.env` should contain:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

Restart Vite after changing `.env`.

## Filtered API example

```text
GET /api/v1/transactions?q=rent&type=expense&start_date=2026-01-01&end_date=2026-12-31&sort=amount_high&skip=0&limit=20
```

Supported `sort` values: `newest`, `oldest`, `amount_high`, `amount_low`, `name`.

## Run backend validation tests

From `backend` with the virtual environment active:

```cmd
pytest -q
```

## GitHub submission

From project root:

```cmd
git status
git add .
git commit -m "Day 26: complete features, validation, filtering and optimization"
git push
```

## Optimization notes

- Filtering uses O(n) scan on currently loaded browser records; sorting is O(n log n).
- Pagination limits visible table rows to 10.
- Backend SQL filters narrow records before response serialization.
- Composite indexes support common date/type/category filters.
- `useMemo` caches filtered and sorted rows until dependencies change.
- Axios and CRUD service centralize repeated networking and persistence logic.

## Scope / production notes

- Workspace switcher remains a UI demonstration; authentication and tenant isolation are not implemented.
- AI Insights contains deterministic summaries, not LLM-generated financial advice.
- Customer/supplier ledger balances are not implemented.
- `Base.metadata.create_all()` remains for this training project; use Alembic migrations in production.
- Tests/build must be run in your local environment; this archive has not been executed on your machine.
