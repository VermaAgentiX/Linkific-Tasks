# Day 17 – Postman Testing Guide

## Start services

Backend (PowerShell, from `backend`):
```powershell
uvicorn main:app --reload
```

Frontend (PowerShell, from `frontend`):
```powershell
npm install
npm run dev
```

Base API URL: `http://127.0.0.1:8000`

For protected endpoints, set **Authorization → Bearer Token** to the `access_token` returned by login/register.

## Requests

### 1. Health check
`GET http://127.0.0.1:8000/health`
Expected: `200`
```json
{"status":"ok","database":"connected"}
```

### 2. Register
`POST http://127.0.0.1:8000/auth/register`
Body → raw → JSON:
```json
{
  "name": "Day17 Test User",
  "email": "day17.user@example.com",
  "password": "TestPass123!"
}
```
Expected: `201`. Copy `access_token`. If the email already exists, use another unique email or login.

### 3. Login
`POST http://127.0.0.1:8000/auth/login`
```json
{
  "email": "day17.user@example.com",
  "password": "TestPass123!"
}
```
Expected: `200`. Copy token.

### 4. Create student
`POST http://127.0.0.1:8000/students` (Bearer token required)
```json
{
  "name": "Aarav Sharma",
  "age": 21,
  "course": "Computer Science",
  "email": "aarav.day17@example.com"
}
```
Expected: `201`. Note the returned `id`.

### 5. List students
`GET http://127.0.0.1:8000/students`
Expected: `200` and a JSON array.

### 6. Search students
`GET http://127.0.0.1:8000/students?q=Aarav`
Expected: `200`; matching records.

### 7. Get one student (fixed Day 17 issue)
`GET http://127.0.0.1:8000/students/1`
Replace `1` with the ID returned by create. Bearer token required.
Expected: `200` and one student object.

### 8. Update student
`PUT http://127.0.0.1:8000/students/1`
Replace ID as needed.
```json
{
  "name": "Aarav Sharma Updated",
  "age": 22,
  "course": "Artificial Intelligence",
  "email": "aarav.updated@example.com"
}
```
Expected: `200`.

### 9. Delete student
`DELETE http://127.0.0.1:8000/students/1`
Replace ID as needed.
Expected: `200`.

## Negative/debugging tests

| Request | Expected |
|---|---:|
| `GET /students/0` | 422 |
| `GET /students/999999` (nonexistent ID) | 404 |
| `GET /students` without Bearer token | 401 |
| `POST /students` with `"age": 0` | 422 |
| `POST /students` with extra field `"role": "admin"` | 422 |
| Login with wrong password | 401 |
| Duplicate registration email | 409 |

## Database verification (psql)
After creating a student:
```sql
SELECT id, name, age, course, email, owner_id
FROM students
ORDER BY id DESC;
```
After update, rerun the query. After delete, confirm the record is gone.
