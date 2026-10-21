# Student Record Manager — Linkific Day 7 & Day 8

A full-stack student CRUD application built by extending the Day 6 FastAPI fundamentals project. The React frontend uses reusable components and Tailwind CSS.

## Features
- Create, read, update and delete student records
- Search by student ID, name, course or email
- Pydantic request validation and useful HTTP errors
- Responsive dashboard, summary cards and reusable React components
- FastAPI interactive API docs at `/docs`
- React state and effects with `useState` and `useEffect`

## Tech stack
- Python, FastAPI, Pydantic, Uvicorn
- React, Vite, JavaScript
- Tailwind CSS, Lucide React
- REST API / JSON / Fetch API

## Project structure
```text
Student-Record-Manager-Day7-Day8/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Content.jsx
│   │   │   ├── StudentForm.jsx
│   │   │   └── StudentTable.jsx
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
└── README.md
```

## Run locally

### 1. Start FastAPI (terminal 1)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
API: `http://127.0.0.1:8000`  
Swagger docs: `http://127.0.0.1:8000/docs`

### 2. Start React (terminal 2)
```powershell
cd frontend
npm install
npm run dev
```
Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/students` | List all students |
| GET | `/students?q=aditi` | Search student records |
| GET | `/students/{student_id}` | Retrieve one record |
| POST | `/students` | Create a record |
| PUT | `/students/{student_id}` | Update a record |
| DELETE | `/students/{student_id}` | Delete a record |

### Example JSON body
```json
{
  "name": "Aditi Sharma",
  "age": 21,
  "course": "Computer Science",
  "email": "aditi@example.com"
}
```

## Notes
This learning version stores records in a Python list in memory. Records reset when the backend restarts. A database such as SQLite can be added later. Configure `VITE_API_URL` if the backend is hosted elsewhere.

## Week 1 learning outcomes
- FastAPI routes, HTTP methods, request bodies, validation and status codes
- CRUD operations and searching a Python list
- React components, props, state, event handlers and effects
- Frontend/backend communication using `fetch`
- Tailwind utility classes and responsive layout
- Project structure and GitHub documentation
