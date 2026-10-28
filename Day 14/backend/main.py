
import os
from datetime import datetime, timedelta, timezone
from typing import List

import jwt
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Student Record Manager API",
    description="Student CRUD API with JWT authentication for learning purposes.",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SECRET_KEY = os.getenv("JWT_SECRET_KEY", "LOCAL-ONLY-CHANGE-ME-USE-A-RANDOM-SECRET")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))
password_hasher = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)


class RegisterInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginInput(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic


class StudentInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=2, max_length=100)
    email: EmailStr


class Student(StudentInput):
    id: int



users_by_email = {}
next_user_id = 1
students: List[Student] = []
student_owner_by_id = {}
next_student_id = 1


def create_access_token(user: dict) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user["id"]), "email": user["email"], "exp": expires}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required. Please log in.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub", ""))
    except (InvalidTokenError, ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    for user in users_by_email.values():
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User account was not found. Please register again.",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.get("/")
def home():
    return {"project": "Student Record Manager", "version": app.version, "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/auth/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterInput):
    global next_user_id
    email = str(data.email).strip().lower()
    if email in users_by_email:
        raise HTTPException(status_code=409, detail="An account with this email already exists.")
    user = {
        "id": next_user_id,
        "name": data.name.strip(),
        "email": email,
        "hashed_password": password_hasher.hash(data.password),
    }
    next_user_id += 1
    users_by_email[email] = user
    public_user = UserPublic(id=user["id"], name=user["name"], email=user["email"])
    return TokenResponse(access_token=create_access_token(user), user=public_user)


@app.post("/auth/login", response_model=TokenResponse)
def login(data: LoginInput):
    email = str(data.email).strip().lower()
    user = users_by_email.get(email)
    if not user or not password_hasher.verify(data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    public_user = UserPublic(id=user["id"], name=user["name"], email=user["email"])
    return TokenResponse(access_token=create_access_token(user), user=public_user)


@app.get("/auth/me", response_model=UserPublic)
def get_me(current_user: dict = Depends(get_current_user)):
    return UserPublic(id=current_user["id"], name=current_user["name"], email=current_user["email"])


@app.get("/stats")
def get_dashboard_stats(current_user: dict = Depends(get_current_user)):
    owned_students = [
        student for student in students
        if student_owner_by_id.get(student.id) == current_user["id"]
    ]
    course_names = {student.course.strip().lower() for student in owned_students}
    ages = [student.age for student in owned_students]
    return {
        "total_students": len(owned_students),
        "total_courses": len(course_names),
        "average_age": round(sum(ages) / len(ages), 1) if ages else 0,
    }


@app.get("/students", response_model=List[Student])
def get_students(q: str = "", current_user: dict = Depends(get_current_user)):
    search_term = q.strip().lower()
    owned_students = [
        student for student in students
        if student_owner_by_id.get(student.id) == current_user["id"]
    ]
    if not search_term:
        return owned_students
    return [
        student for student in owned_students
        if search_term in student.name.lower()
        or search_term in student.course.lower()
        or search_term in student.email.lower()
        or search_term == str(student.id)
    ]


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int, current_user: dict = Depends(get_current_user)):
    for student in students:
        if student.id == student_id and student_owner_by_id.get(student.id) == current_user["id"]:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student_data: StudentInput, current_user: dict = Depends(get_current_user)):
    global next_student_id
    student = Student(id=next_student_id, **student_data.model_dump())
    students.append(student)
    student_owner_by_id[student.id] = current_user["id"]
    next_student_id += 1
    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(
    student_id: int,
    student_data: StudentInput,
    current_user: dict = Depends(get_current_user),
):
    for index, student in enumerate(students):
        if student.id == student_id and student_owner_by_id.get(student.id) == current_user["id"]:
            updated = Student(id=student_id, **student_data.model_dump())
            students[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int, current_user: dict = Depends(get_current_user)):
    for index, student in enumerate(students):
        if student.id == student_id and student_owner_by_id.get(student.id) == current_user["id"]:
            students.pop(index)
            student_owner_by_id.pop(student_id, None)
            return {"message": "Student deleted successfully", "id": student_id}
    raise HTTPException(status_code=404, detail="Student not found")
