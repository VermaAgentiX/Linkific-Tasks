# API Reference

Base URL for local development: `http://127.0.0.1:8000`

Interactive API docs: `/docs` (Swagger UI) and `/redoc` (ReDoc).

Protected endpoints require this header:

```http
Authorization: Bearer <access_token>
```

## Health and service

### `GET /`
Returns the API welcome/status response.

### `GET /health`
Checks application/database health.

## Authentication

### `POST /auth/register`
Creates a user and returns an access token.

```json
{
  "name": "Demo User",
  "email": "demo@example.com",
  "password": "ExamplePass123!"
}
```

Success: `201 Created`.

### `POST /auth/login`
Authenticates an existing user and returns an access token.

```json
{
  "email": "demo@example.com",
  "password": "ExamplePass123!"
}
```

Success: `200 OK`.

### `POST /auth/logout`
Logs out the current client session (JWT-based clients should discard the token).

Authentication required.

### `GET /auth/me`
Returns the authenticated user's public profile.

Authentication required.

## Administration

### `GET /admin/users`
Returns the user list for administrators.

Authentication and administrator role required.

## Dashboard

### `GET /stats`
Returns dashboard statistics for the authenticated user.

Authentication required.

## Students

Student routes require authentication and are scoped to the current user.

### `GET /students`
Lists the current user's student records. Optional search query:

```http
GET /students?q=computer
```

### `GET /students/{student_id}`
Returns one student owned by the current user. The ID must be positive.

### `POST /students`
Creates a student record.

```json
{
  "name": "Aarav Sharma",
  "age": 21,
  "course": "Computer Science",
  "email": "aarav@example.com"
}
```

Success: `201 Created`.

### `PUT /students/{student_id}`
Updates a student owned by the current user.

```json
{
  "name": "Aarav Sharma",
  "age": 22,
  "course": "Artificial Intelligence",
  "email": "aarav.updated@example.com"
}
```

### `DELETE /students/{student_id}`
Deletes a student owned by the current user.

## Common responses

| Status | Meaning |
|---|---|
| 200 | Request succeeded |
| 201 | Resource created |
| 401 | Missing or invalid authentication |
| 403 | Insufficient permissions |
| 404 | Resource not found or not accessible |
| 409 | Conflict, such as duplicate registration |
| 422 | Request validation failed |
| 500 | Unexpected server error |

Exact response schemas are available from the running OpenAPI documentation at `/docs`.
