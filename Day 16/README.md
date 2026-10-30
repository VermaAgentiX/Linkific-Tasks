# Day 16 -- Validation & Error Handling

## Student Record Manager

**Internship:** Linkific -- Python Full-Stack Developer\
**Day:** 16\
**Date:** 30 October 2026\
**Project:** Student Record Manager

------------------------------------------------------------------------

## 1. Overview

The objective of Day 16 is to improve the reliability and stability of
the Student Record Manager by implementing frontend form validation,
backend request validation, and proper API error handling.

The application validates user input before processing requests and
provides meaningful error responses when invalid data or unexpected
errors occur.

## 2. Objectives

-   Implement frontend form validation.
-   Implement backend request validation using Pydantic.
-   Validate required fields and user inputs.
-   Handle API errors gracefully.
-   Display user-friendly error messages.
-   Handle database transaction failures.
-   Test validation and error responses using Postman.
-   Improve overall application stability.

## 3. Technology Stack

  Technology   Purpose
  ------------ ------------------------
  React        Frontend UI
  JavaScript   Client-side validation
  FastAPI      Backend REST API
  Python       Backend logic
  Pydantic     Request validation
  PostgreSQL   Database
  SQLAlchemy   Database ORM
  Postman      API testing
  JWT          Authentication

## 4. Validation Implementation

### Frontend Validation

The frontend should validate form inputs before sending requests to the
backend.

Examples:

-   Name cannot be empty.
-   Email must follow a valid email format.
-   Age must be a valid integer.
-   Course name is required.
-   Password must satisfy the minimum length requirement.

### Backend Validation

Backend validation provides an additional layer of security and data
integrity.

FastAPI and Pydantic are used to validate incoming request data.

Examples:

-   Required field validation.
-   Data type validation.
-   Email format validation.
-   Age range validation.
-   Invalid request rejection.

**Note:** Backend validation must remain authoritative even when
frontend validation is enabled.

## 5. Error Handling

The application handles common API and database errors.

  HTTP Status   Description
  ------------- -----------------------------
  400           Bad Request
  401           Unauthorized
  403           Forbidden
  404           Resource Not Found
  409           Conflict / Duplicate Record
  422           Validation Error
  500           Internal Server Error

Database operations should use proper exception handling and transaction
rollback to prevent incomplete database changes.

## 6. API Testing with Postman

The following endpoints can be used to test the application.

**Base URL:**

``` text
http://127.0.0.1:8000
```

  Method   Endpoint           Purpose
  -------- ------------------ --------------------------
  POST     `/auth/register`   Register a user
  POST     `/auth/login`      Authenticate user
  GET      `/auth/me`         Get current user
  GET      `/students`        Retrieve student records
  POST     `/students`        Create a student
  PUT      `/students/{id}`   Update student details
  DELETE   `/students/{id}`   Delete a student

### Example: Valid Student Request

**POST** `/students`

``` json
{
  "name": "Rahul Sharma",
  "age": 21,
  "course": "Computer Science",
  "email": "rahul@example.com"
}
```

### Example: Invalid Student Request

**POST** `/students`

``` json
{
  "name": "",
  "age": 0,
  "course": "",
  "email": "invalid-email"
}
```

Expected response: `422 Unprocessable Entity`, provided the
corresponding Pydantic field constraints are configured.

## 7. Database Error Handling

PostgreSQL is used to store user and student records.

SQLAlchemy transaction handling helps maintain database consistency.

Important practices:

-   Handle database exceptions.
-   Roll back failed transactions.
-   Prevent duplicate records.
-   Return meaningful error responses.
-   Avoid exposing sensitive database details to clients.

## 8. Running the Application

### Backend

``` bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

``` bash
cd frontend
npm install
npm run dev
```

### API Documentation

Open the FastAPI Swagger documentation:

<http://127.0.0.1:8000/docs>

## 9. Testing Checklist

-   [ ] Test valid form submissions.
-   [ ] Test empty required fields.
-   [ ] Test invalid email addresses.
-   [ ] Test invalid age values.
-   [ ] Test invalid API requests.
-   [ ] Test duplicate user registration.
-   [ ] Test unauthorized API requests.
-   [ ] Test database transaction rollback.
-   [ ] Verify database records after CRUD operations.
-   [ ] Verify user-friendly error messages.
-   [ ] Update GitHub repository.

## 10. Learning Outcomes

Through this task, I learned:

-   The importance of frontend and backend validation.
-   How Pydantic validates incoming API requests.
-   How FastAPI handles HTTP exceptions.
-   How to manage database errors using SQLAlchemy.
-   Why transaction rollback is important.
-   How to test API validation using Postman.
-   How proper error handling improves application reliability.

------------------------------------------------------------------------

**Day 16 -- Validation & Error Handling**\
*Linkific Python Full-Stack Developer Internship*
