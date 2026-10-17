# Linkific Internship — Day 6: FastAPI Fundamentals

A beginner-friendly REST API built with **FastAPI** and **Pydantic** to practice backend fundamentals, HTTP methods, JSON request bodies, validation, and Postman testing.

## Features

- `GET /` — return a welcome message
- `GET /students` — return all student records
- `GET /students/{student_id}` — return one student by ID
- `POST /students` — create a student with request validation
- Interactive API documentation at `/docs`

## Tech Stack

- Python
- FastAPI
- Pydantic
- Postman

## Project Structure

```text
day6_fastapi/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── postman_collection.json
```

## Setup and Run

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Start the development server

```powershell
fastapi dev main.py
```

The API should be available at `http://127.0.0.1:8000`.

Open `http://127.0.0.1:8000/docs` to explore and test the endpoints in the browser.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/students` | List all students |
| GET | `/students/{student_id}` | Get a student by ID |
| POST | `/students` | Create a student |

### Example POST request body

Send this JSON to `POST /students`:

```json
{
  "name": "Abhishek",
  "age": 23,
  "course": "Computer Science"
}
```

A successful create request returns **201 Created**.

## Test with Postman

1. Open Postman and select **Import**.
2. Import `postman_collection.json`.
3. Ensure the FastAPI server is running.
4. Test **Home**, **Get All Students**, **Create Student**, and **Get Student by ID**.
5. For the POST request, select **Body → raw → JSON** and use the sample body above.

The collection uses `http://127.0.0.1:8000` as its base URL.

## Concepts Practiced

- REST API fundamentals and client-server communication
- Routes, path parameters, and query parameters
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- JSON request and response bodies
- Pydantic models and input validation
- Postman request testing and HTTP status codes
- Python list reversal and maximum value
- Merging sorted arrays with two pointers
- Removing duplicates while preserving order
- JavaScript Fetch API, `async/await`, and `response.ok`

## Limitations

Student records are stored in a Python list in memory. They are not persisted to a database and will reset when the server restarts. This project is for learning and demonstration, not production use.

## Learning Outcome

Built and tested a small FastAPI backend, practiced request validation and HTTP methods, and reviewed how frontend JavaScript can communicate with backend APIs.
