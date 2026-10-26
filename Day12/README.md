# Day12 - Student Record Manager Updated endpoints and FastApi connections 

A full-stack student management application built with **React**,
**React Router**, and **FastAPI**. The application demonstrates
client--server communication, REST API integration, CRUD operations,
search, dashboard statistics, and frontend loading/error feedback.

## Features

-   **Dashboard:** Displays student statistics, including total
    students, course count, and average age.
-   **Student management:** Create, view, update, and delete student
    records.
-   **Search:** Filter students by name, course, email, or student ID.
-   **Multi-page navigation:** React Router routes for the dashboard,
    student list, add/edit forms, details, and About page.
-   **API integration:** A shared frontend API helper communicates with
    FastAPI using the Fetch API.
-   **Validation:** Pydantic models validate incoming student data.
-   **Loading and error feedback:** The UI shows request status and
    helpful errors when the API cannot be reached or rejects a request.
-   **API documentation:** FastAPI provides interactive documentation
    through Swagger UI.

## Technology Stack

  -----------------------------------------------------------------------
  Layer                               Technologies
  ----------------------------------- -----------------------------------
  Frontend                            React, JavaScript, React Router,
                                      Vite

  API client                          Fetch API

  Backend                             Python, FastAPI, Uvicorn

  Data validation                     Pydantic

  API testing                         FastAPI Swagger UI; Postman can be
                                      used for manual endpoint testing

  Styling                             CSS, Tailwind configuration
  -----------------------------------------------------------------------

## Project Structure

``` text
Student-Record-Manager/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Footer.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── StatCard.jsx
│   │   │   ├── StudentForm.jsx
│   │   │   └── StudentTable.jsx
│   │   ├── pages/
│   │   │   ├── AboutPage.jsx
│   │   │   ├── AddStudentPage.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── EditStudentPage.jsx
│   │   │   ├── NotFoundPage.jsx
│   │   │   ├── StudentDetailsPage.jsx
│   │   │   └── StudentsPage.jsx
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── .env.example
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Getting Started

### Prerequisites

Install the following before running the project:

-   Python 3.10 or newer (use a version compatible with the installed
    FastAPI/Pydantic dependencies)
-   Node.js and npm
-   Git (optional, for version control)

### 1. Start the FastAPI backend

From the repository root, open a terminal:

**Windows PowerShell**

``` powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

**macOS/Linux**

``` bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

The backend will normally be available at:

-   API base URL: `http://127.0.0.1:8000`
-   Health check: `http://127.0.0.1:8000/health`
-   Interactive API documentation: `http://127.0.0.1:8000/docs`

A successful health check returns:

``` json
{"status": "ok"}
```

### 2. Configure and start the React frontend

Open a **second terminal** at the repository root:

``` bash
cd frontend
npm install
```

The frontend uses `VITE_API_URL` to determine the backend URL. The
default is `http://127.0.0.1:8000`. To override it, create a `.env` file
inside `frontend/`:

``` env
VITE_API_URL=http://127.0.0.1:8000
```

Then start the development server:

``` bash
npm run dev
```

Open the URL printed by Vite, usually `http://localhost:5173`.

> Restart the Vite server after changing `.env` values. Vite exposes
> client-side environment variables prefixed with `VITE_`; do not put
> secrets in them.

## Frontend Routes

  Route                  Description
  ---------------------- -----------------------------------
  `/`                    Dashboard and summary statistics
  `/students`            Search and manage student records
  `/students/new`        Create a student record
  `/students/:id`        View a student's details
  `/students/:id/edit`   Edit a student record
  `/about`               Project information
  `*`                    Not-found page

## REST API Reference

Base URL: `http://127.0.0.1:8000`

  --------------------------------------------------------------------------
  Method                  Endpoint                   Description
  ----------------------- -------------------------- -----------------------
  `GET`                   `/`                        API information and
                                                     version

  `GET`                   `/health`                  Check backend health

  `GET`                   `/stats`                   Dashboard statistics

  `GET`                   `/students`                Retrieve all students

  `GET`                   `/students?q=alex`         Search by name, course,
                                                     email, or ID

  `GET`                   `/students/{student_id}`   Retrieve one student

  `POST`                  `/students`                Create a student

  `PUT`                   `/students/{student_id}`   Update a student's
                                                     editable fields

  `DELETE`                `/students/{student_id}`   Delete a student
  --------------------------------------------------------------------------

### Example: Create a Student

Send a `POST` request to `/students` with a JSON body:

``` json
{
  "name": "Alex Morgan",
  "age": 21,
  "course": "Computer Science",
  "email": "alex@example.com"
}
```

The API validates the request and returns the created record, including
its generated `id`.

### Example: Update a Student

Send a `PUT` request to `/students/1` with the required student fields:

``` json
{
  "name": "Alex Morgan",
  "age": 22,
  "course": "Artificial Intelligence",
  "email": "alex@example.com"
}
```

## React--FastAPI Data Flow

1.  A user opens a page or performs an action in the React interface.
2.  A page or shared handler calls a method from `frontend/src/api.js`.
3.  The helper sends an HTTP request using `fetch`.
4.  FastAPI receives the request, validates input with Pydantic where
    applicable, and executes the endpoint logic.
5.  FastAPI returns a JSON response or an HTTP error.
6.  React updates component state and renders the latest data or a
    helpful error message.

## CORS Configuration

The backend currently allows these local development origins:

-   `http://localhost:5173`
-   `http://127.0.0.1:5173`

If the frontend runs on a different origin or port, update the
`allow_origins` list in `backend/main.py`. In production, configure CORS
for the exact frontend domain rather than allowing every origin.

## Testing Checklist

-   [ ] Start the backend and confirm `/health` returns
    `{"status":"ok"}`.
-   [ ] Open `/docs` and inspect the available endpoints.
-   [ ] Verify the dashboard and student list load data.
-   [ ] Create a student and confirm it appears in the list.
-   [ ] Search for a student by name or course.
-   [ ] Open a student's detail page.
-   [ ] Update a student and verify the new values.
-   [ ] Delete a student and verify it is removed.
-   [ ] Stop the backend temporarily and confirm the frontend displays a
    connection error.
-   [ ] Optionally save the tested requests in a Postman collection.

## Known Limitations

-   **In-memory storage:** Student records are stored in a Python list
    and reset when the backend process restarts.
-   **Local development CORS:** The configured origins are for local
    development and may need to be changed for deployment.
-   **No authentication:** The project is a learning application and
    does not currently include user authentication or authorization.
-   **Testing status:** Run the application and complete the checklist
    above before claiming all flows are verified. A Postman collection
    should only be linked if it has actually been created and committed.

## Future Improvements

-   Add persistent storage with SQLite or PostgreSQL.
-   Add automated backend tests with `pytest` and frontend tests.
-   Add pagination and more advanced filtering.
-   Add authentication and role-based access control.
-   Add deployment instructions and environment-specific configuration.

## Learning Outcomes

This project provides hands-on practice with React components and hooks,
client-side routing, REST APIs, HTTP methods, JSON request/response
handling, FastAPI routing, Pydantic validation, CORS, loading/error
states, and full-stack debugging.

## License

Add a license file if you intend to publish or distribute this project
under a specific open-source license.
