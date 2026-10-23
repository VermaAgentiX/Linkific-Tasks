# Student Record Manager - CRUD Updation using FASTAPI

A beginner-friendly full-stack student management application built with React, React Router, and FastAPI. This version keeps the code organized into small files with descriptive names and comments where they help explain the intent.

## Features

- Dashboard with dynamic student statistics and recently added records
- Student list with search by name, course, email, or ID
- Add, view, edit, and delete student records
- React Router navigation and a not-found page
- React `useState` and `useEffect`
- FastAPI CRUD endpoints with Pydantic validation
- Responsive dashboard layout
- Clear loading, error, and success feedback

## Project structure

```text
Student-Record-Manager-Humanized/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── StudentForm.jsx
│   │   │   ├── StudentTable.jsx
│   │   │   └── StatCard.jsx
│   │   ├── pages/
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── StudentsPage.jsx
│   │   │   ├── AddStudentPage.jsx
│   │   │   ├── EditStudentPage.jsx
│   │   │   ├── StudentDetailsPage.jsx
│   │   │   ├── AboutPage.jsx
│   │   │   └── NotFoundPage.jsx
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
└── README.md
```

## Run on Windows

### 1. Start the backend

Open a terminal at the project root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

FastAPI: http://127.0.0.1:8000  
Interactive API docs: http://127.0.0.1:8000/docs

### 2. Start the frontend

Open a second terminal at the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, usually http://localhost:5173.

## Routes

| Route | Purpose |
|---|---|
| `/` | Dashboard |
| `/students` | Search and manage student records |
| `/students/new` | Add a student |
| `/students/:id` | View a student |
| `/students/:id/edit` | Edit a student |
| `/about` | Project and concept notes |
| Any unknown route | 404 page |

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/stats` | Dashboard statistics |
| GET | `/students` | List records |
| GET | `/students?q=alex` | Search records |
| GET | `/students/{student_id}` | Get one record |
| POST | `/students` | Create a record |
| PUT | `/students/{student_id}` | Update a record |
| DELETE | `/students/{student_id}` | Delete a record |

## Storage limitation

Records are stored in a Python list in memory. They reset when the backend restarts. SQLite or another database can be added when persistence is required.
