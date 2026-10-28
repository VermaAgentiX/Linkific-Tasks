# Student Record Manager — Day 14 Weekly Assessment

A full-stack Student Record Manager built with React and FastAPI, featuring user authentication, protected routes, student CRUD operations, search, and database integration.

## Overview

The goal of Day 14 was to improve the Student Record Manager based on client requirements, strengthen backend integration, configure PostgreSQL, and prepare the application for testing.

## Features

- **User Authentication:** Registration and login using JWT authentication.
- **Protected Routes:** Restrict access to authenticated users.
- **Student Management:** Create, read, update, and delete student records.
- **Search:** Search student records using supported fields.
- **Database Integration:** PostgreSQL database configuration using SQLAlchemy.
- **Password Security:** Argon2 password hashing.
- **API Documentation:** Interactive API documentation through FastAPI Swagger UI.
- **Responsive Interface:** React-based dashboard and reusable UI components.
- **Error Handling:** API validation and error handling.

## Technology Stack

### Frontend
- React
- JavaScript
- HTML5
- CSS3

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PyJWT
- pwdlib with Argon2

### Database
- PostgreSQL 18
- SQLite fallback for local development, if configured by the application

### Tools
- Visual Studio Code
- Git and GitHub
- PowerShell
- psql
- FastAPI Swagger UI

## Project Structure

```text
Student-Record-Manager/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
└── README.md
```

*Note: Adjust the frontend structure above to match the actual files in your repository. The backend modules should be present in your local project before using this structure.*

## Prerequisites

- Python 3.10 or later, compatible with the installed dependencies
- Node.js and npm
- PostgreSQL 18
- Git

## PostgreSQL Configuration

Create the project database using `psql`:

```sql
CREATE DATABASE student_record_manager;
```

Connect to the database:

```sql
\c student_record_manager
```

Check the tables:

```sql
\dt
```

Create a `.env` file inside the backend directory:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/student_record_manager
JWT_SECRET_KEY=replace-with-a-strong-random-secret
JWT_EXPIRE_MINUTES=60
```

Replace the placeholders with your local configuration. URL-encode special characters in the database password when required.

**Security:** Do not commit `.env` or expose database credentials and JWT secrets in GitHub.

## Backend Setup

Open a terminal in the backend directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Check Python syntax:

```powershell
python -m py_compile main.py database.py models.py schemas.py
```

Start the FastAPI development server:

```powershell
uvicorn main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

## Frontend Setup

Open another terminal in the frontend directory:

```powershell
npm install
npm run dev
```

Open the local URL displayed by Vite or your configured React development server.

Ensure the frontend API base URL points to the running FastAPI backend.

## API Endpoints

The intended API functionality includes the following routes. Confirm the exact paths and methods in `main.py` or `/docs` before testing.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Authenticate a user |
| GET | `/auth/me` | Get the current authenticated user |
| GET | `/students` | List/search student records |
| POST | `/students` | Create a student record |
| GET | `/students/{id}` | Retrieve a student record, if implemented |
| PUT/PATCH | `/students/{id}` | Update a student record |
| DELETE | `/students/{id}` | Delete a student record |
| GET | `/stats` | Retrieve dashboard statistics, if implemented |
| GET | `/health` | Check application health |

Protected endpoints should receive a valid JWT access token using the Bearer authorization scheme.

## Testing Checklist

- [ ] PostgreSQL service is running.
- [ ] Backend `.env` points to `student_record_manager`.
- [ ] SQLAlchemy tables exist in the intended database.
- [ ] Backend dependencies install successfully.
- [ ] FastAPI starts without errors.
- [ ] User registration works.
- [ ] Login returns a valid access token.
- [ ] Protected routes reject unauthenticated requests.
- [ ] Student create, read, update, and delete operations work.
- [ ] Search returns the expected records.
- [ ] Each user can access only their own student records.
- [ ] Frontend and backend communicate successfully.
- [ ] Data persists after restarting the backend.

## Day 14 Learning Outcomes

- Learned how to install and verify PostgreSQL on Windows.
- Practised connecting to PostgreSQL using `psql`.
- Learned to list databases, switch databases, and inspect tables.
- Investigated a table-not-found error caused by querying the wrong database context.
- Reviewed the responsibilities of SQLAlchemy database configuration, ORM models, and Pydantic schemas.
- Prepared the backend for database connectivity, JWT authentication, and account-scoped student CRUD testing.

## Current Progress

PostgreSQL 18.6 is installed, its Windows service is running, and the `student_record_manager` database exists. The FastAPI health endpoint has returned `{"status":"ok"}`.

The live PostgreSQL connection from FastAPI, presence of the expected tables, authentication flows, and complete CRUD functionality still need to be verified before marking those tests as passed.

## Future Improvements

- Add automated backend tests using pytest.
- Use Alembic for database schema migrations.
- Improve API validation and error messages.
- Add pagination and sorting for larger student datasets.
- Deploy the frontend and backend.
- Configure production secrets and database credentials securely.

## Author

**Abhishek Verma**  
Linkific Internship — Day 14 Weekly Assessment

## License

This project was developed as part of an internship learning and assessment task.
