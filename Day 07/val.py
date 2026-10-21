
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request body schema
class Student(BaseModel):
    name: str
    age: int
    course: str

# Temporary in-memory storage
students = []

# GET: retrieve all students
@app.get("/students")
def get_students():
    return students

# POST: create a student
@app.post("/students", status_code=201)
def create_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student created successfully",
        "student": student
    }
