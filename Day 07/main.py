#starting app - fastapi dev main.py

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Linkific Student API")

# Serve the landing page
@app.get("/intro")
async def home():
    return FileResponse("index.html")




@app.get("/")
def about():
    return {
        "project": "Linkific Day 6",
        "topic": "FastAPI Fundamentals"
    }


class Student(BaseModel):
    name: str
    age: int
    course: str


students = []


@app.get("/students")
def get_students():
    return students


@app.post("/students", status_code=201)
def create_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student created successfully",
        "student": student
    }


@app.get("/search")
def search_student(name: str, age: int = 0):
    return {
        "name": name,
        "age": age
    }
