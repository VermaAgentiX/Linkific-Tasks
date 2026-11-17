# FinanceFlow AI — API Reference

**API version:** `0.4.0`  
**Base URL (local):** `http://localhost:8000/api/v1`  
**Interactive reference:** `http://localhost:8000/docs` (Swagger UI)  
**Alternative reference:** `http://localhost:8000/redoc`

The running FastAPI application generates its OpenAPI schema at `/openapi.json`. Swagger and ReDoc are the authoritative interactive references for the exact request and response schemas.

## Conventions

- Request and response bodies use JSON unless an endpoint returns `204 No Content`.
- Resource identifiers are integer IDs.
- Dates use ISO 8601 calendar format: `YYYY-MM-DD`.
- Monetary amounts are positive decimal values with up to two decimal places.
- Validation errors return HTTP `422`.
- A missing resource returns HTTP `404`.
- List endpoints accept `skip` (default `0`) and `limit` (default `100`, maximum `500`).

## Health

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Basic service status and docs path |
| `GET` | `/health` | Basic health status |
| `GET` | `/api/v1/health` | Versioned health status |

## Resource endpoints

The same CRUD pattern is available for each resource:

| Resource | Collection endpoint |
|---|---|
| Categories | `/categories` |
| Transactions | `/transactions` |
| Customers | `/customers` |
| Suppliers | `/suppliers` |
| Budgets | `/budgets` |

For each collection endpoint:

| Method | Path | Result |
|---|---|---|
| `GET` | `/{resource}` | List records |
| `POST` | `/{resource}` | Create a record (`201`) |
| `GET` | `/{resource}/{id}` | Retrieve one record |
| `PUT` | `/{resource}/{id}` | Update supplied fields |
| `DELETE` | `/{resource}/{id}` | Delete a record (`204`) |

### Transaction list filters

`GET /transactions` supports:

| Parameter | Values / format | Description |
|---|---|---|
| `q` | text, 1–100 chars | Matches title, account, or payment method |
| `type` | `income` or `expense` | Filters transaction type |
| `start_date` | `YYYY-MM-DD` | Inclusive lower date bound |
| `end_date` | `YYYY-MM-DD` | Inclusive upper date bound |
| `sort` | `newest`, `oldest`, `amount_high`, `amount_low`, `name` | Sort order |
| `skip` | integer ≥ 0 | Number of records to skip |
| `limit` | integer 1–500 | Maximum records to return |

Example:

```http
GET /api/v1/transactions?q=rent&type=expense&start_date=2026-01-01&end_date=2026-12-31&sort=amount_high&skip=0&limit=20
```

### Transaction search

```http
GET /api/v1/transactions/search?q=office
```

Searches transaction title, account, and payment method. The endpoint returns up to 100 matching records.

## Example request bodies

### Create a category

```json
{
  "name": "Office expenses",
  "kind": "expense",
  "color": "#64748b"
}
```

### Create a transaction

```json
{
  "title": "Office rent",
  "amount": "8500.00",
  "type": "expense",
  "category_id": null,
  "date": "2026-11-17",
  "payment_method": "bank",
  "account": "Main account",
  "notes": "November rent"
}
```

### Create a customer

```json
{
  "name": "Sample Customer",
  "phone": "9000000000",
  "email": "customer@example.com",
  "address": "Bhopal",
  "notes": "Example record"
}
```

### Create a budget

```json
{
  "name": "Monthly groceries",
  "amount": "6000.00",
  "period": "monthly",
  "category_id": null,
  "start_date": "2026-11-01",
  "end_date": "2026-11-30"
}
```

## Error response examples

Validation errors are normalized by the API into a `detail` array:

```json
{
  "detail": [
    {
      "field": "body.amount",
      "message": "Input should be greater than 0",
      "type": "greater_than"
    }
  ]
}
```

A missing resource returns a `404` response. Database constraint conflicts may return `409`, depending on the operation and database constraint.

## Important scope notes

- The current API is a learning-project CRUD API. It does not implement authentication or per-user workspace authorization.
- Do not expose it publicly with real financial data until authentication, authorization, tenant isolation, HTTPS, secret management, and production database migrations are implemented.
- The project uses `Base.metadata.create_all()` for convenient local setup. Use Alembic migrations for deployed environments.
