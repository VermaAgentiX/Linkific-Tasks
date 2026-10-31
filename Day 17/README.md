# Day 17 -- Testing & Debugging Using Postman

## Student Record Manager

**Internship:** Linkific -- Python Full-Stack Developer\
**Day:** 17\
**Date:** 31 October 2026

------------------------------------------------------------------------

## 1. Overview

Day 17 focused on debugging and testing the Student Record Manager, a
React frontend connected to a FastAPI backend and PostgreSQL database.

The task involved reviewing existing functionality, identifying API
issues, fixing the discovered issue, preparing API tests in Postman, and
documenting the debugging work.

## 2. Objectives

-   Learn and apply debugging techniques.
-   Review and debug existing application issues.
-   Test backend APIs using Postman.
-   Test frontend functionality in the browser.
-   Fix identified bugs.
-   Document resolved issues.
-   Update the GitHub repository.

## 3. Technology Stack

  Technology   Purpose
  ------------ ---------------------------
  React        Frontend
  JavaScript   Frontend logic
  FastAPI      REST API backend
  Python       Backend implementation
  PostgreSQL   Relational database
  SQLAlchemy   Database ORM
  JWT          Authentication
  Postman      API testing
  VS Code      Development and debugging

## 4. Bug Identified and Fixed

### Missing single-student API endpoint

**Issue:** The frontend included a student details view and called the
API client method for retrieving a student by ID, but the backend did
not implement `GET /students/{student_id}`.

**Impact:** The frontend could not retrieve an individual student record
through the API.

**Fix:** Added an authenticated FastAPI endpoint:

``` http
GET /students/{student_id}
```

The endpoint: - Validates that the student ID is positive. - Requires
authentication. - Returns only records belonging to the authenticated
user. - Returns `404 Not Found` when the record does not exist or is not
owned by the current user.

## 5. Postman API Testing

**Base URL:**

``` text
http://127.0.0.1:8000
```

Protected endpoints require a JWT access token. In Postman, select
**Authorization → Bearer Token** and provide the token returned by
registration or login.

  Method   Endpoint              Purpose
  -------- --------------------- ---------------------------
  GET      `/health`             Check backend health
  POST     `/auth/register`      Register a test user
  POST     `/auth/login`         Login and obtain JWT
  GET      `/auth/me`            Verify authenticated user
  GET      `/students`           List student records
  GET      `/students?q=Aarav`   Search students
  GET      `/students/{id}`      Retrieve one student
  POST     `/students`           Create a student
  PUT      `/students/{id}`      Update a student
  DELETE   `/students/{id}`      Delete a student

### Example: Create a student

**POST** `/students`

``` json
{
  "name": "Aarav Sharma",
  "age": 21,
  "course": "Computer Science",
  "email": "aarav.day17@example.com"
}
```

### Example: Update a student

**PUT** `/students/{id}`

``` json
{
  "name": "Aarav Sharma Updated",
  "age": 22,
  "course": "Artificial Intelligence",
  "email": "aarav.updated@example.com"
}
```

## 6. Negative Testing

  Test                                      Expected status
  --------------------------------------- -----------------
  Request `/students/0`                                 422
  Request a nonexistent student ID                      404
  Call protected endpoint without token                 401
  Submit invalid student data                           422
  Login with incorrect password                         401
  Register an already-used email                        409

Actual outcomes should be recorded after running these requests locally.

## 7. Database Verification

After creating, updating, or deleting a student through Postman, verify
the result in PostgreSQL:

``` sql
SELECT id, name, age, course, email, owner_id
FROM students
ORDER BY id DESC;
```

This confirms whether API operations are reflected in the database.

## 8. Running the Application

### Backend

``` powershell
cd backend
uvicorn main:app --reload
```

### Frontend

``` powershell
cd frontend
npm install
npm run dev
```

### API documentation

Open <http://127.0.0.1:8000/docs>.

## 9. Debugging Checklist

-   [ ] Run backend and frontend locally.
-   [ ] Inspect browser console and Network tab.
-   [ ] Test registration and login.
-   [ ] Test student list, search, details, create, update, and delete.
-   [ ] Test invalid IDs and invalid request bodies.
-   [ ] Verify authentication and ownership restrictions.
-   [ ] Verify database records after CRUD operations.
-   [ ] Record actual test results in the bug report.
-   [ ] Commit and push updates to GitHub.

## 10. Deliverables

-   Fixed `GET /students/{student_id}` backend endpoint.
-   `BUG_REPORT_DAY17.md` documenting the issue and fix.
-   `POSTMAN_TESTING.md` containing API test steps and sample data.
-   Updated project documentation and GitHub repository.

## 11. Learning Outcomes

-   Practiced tracing frontend API calls to backend routes.
-   Learned to identify missing API functionality through code review.
-   Practiced positive and negative API testing with Postman.
-   Reinforced authentication and user-ownership checks.
-   Learned to document bugs, fixes, and verification steps.

------------------------------------------------------------------------

**Day 17 -- Testing & Debugging**\
*Linkific Python Full-Stack Developer Internship*
