from typing import List
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Student Record Manager API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=120)

class Student(StudentCreate):
    id: int

students: List[Student] = []
next_id = 1

@app.get("/")
def home():
    return {"project": "Student Record Manager", "version": "1.0.0", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students", response_model=List[Student])
def get_students(q: str = Query(default="", max_length=100)):
    term = q.strip().lower()
    if not term:
        return students
    return [
        st for st in students
        if term in st.name.lower()
        or term in st.course.lower()
        or term in st.email.lower()
        or term == str(st.id)
    ]

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for st in students:
        if st.id == student_id:
            return st
    raise HTTPException(status_code=404, detail="Student not found")



@app.post("/students", response_model=Student, status_code=201)
def create_student(data: StudentCreate):
    global next_id
    st = Student(id=next_id, **data.model_dump())
    students.append(st)
    next_id += 1
    return st




@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, data: StudentCreate):
    for ix, st in enumerate(students):
        if st.id == student_id:
            upd = Student(id=student_id, **data.model_dump())
            students[ix] = upd
            return upd
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for ix, st in enumerate(students):
        if st.id == student_id:
            students.pop(ix)
            return {"message": "Student deleted successfully", "id": student_id}
    raise HTTPException(status_code=404, detail="Student not found")
