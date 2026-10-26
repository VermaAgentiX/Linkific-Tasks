"""
Student Record Manager API
--------------------------
A small FastAPI backend for managing student records.

Note: This learning project uses in-memory storage. Data is reset when
the backend restarts. SQLite can be added when persistent storage is needed.
"""

from typing import List

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="Student Record Manager API",
    description="A beginner-friendly CRUD API for student records.",
    version="2.1.0",
)

# Allow the local React development server to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StudentInput(BaseModel):
    """Fields required when a student is created or updated."""

    name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=120)


class Student(StudentInput):
    """A student record, including its generated ID."""

    id: int


# Temporary storage for this learning project.
students: List[Student] = []
next_student_id = 1


@app.get("/")
def home():
    """Show basic information about the API."""
    return {
        "project": "Student Record Manager",
        "version": app.version,
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    """Let the frontend or developer check whether the API is running."""
    return {"status": "ok"}


@app.get("/stats")
def get_dashboard_stats():
    """Return summary values used by the React dashboard."""
    course_names = {student.course.strip().lower() for student in students}
    ages = [student.age for student in students]

    return {
        "total_students": len(students),
        "total_courses": len(course_names),
        "average_age": round(sum(ages) / len(ages), 1) if ages else 0,
    }


@app.get("/students", response_model=List[Student])
def get_students(q: str = Query(default="", max_length=100)):
    """Return every student, or filter records using a search term."""
    search_term = q.strip().lower()

    if not search_term:
        return students

    return [
        student
        for student in students
        if search_term in student.name.lower()
        or search_term in student.course.lower()
        or search_term in student.email.lower()
        or search_term == str(student.id)
    ]


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """Return one student by ID."""
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", response_model=Student, status_code=201)
def create_student(student_data: StudentInput):
    """Validate and add a new student record."""
    global next_student_id

    student = Student(
        id=next_student_id,
        **student_data.model_dump(),
    )

    students.append(student)
    next_student_id += 1

    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_data: StudentInput):
    """Replace the editable fields for an existing student."""
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_student = Student(
                id=student_id,
                **student_data.model_dump(),
            )
            students[index] = updated_student
            return updated_student

    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """Delete a student record by ID."""
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {
                "message": "Student deleted successfully",
                "id": student_id,
            }

    raise HTTPException(status_code=404, detail="Student not found")
