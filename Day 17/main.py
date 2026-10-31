"""FastAPI API for Student Record Manager — Day 16 validation and error handling."""
import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import Depends, FastAPI, HTTPException, status, Request, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import func, inspect, text, or_
from sqlalchemy.orm import Session



from database import Base, engine, get_db
from models import Student, User
from schemas import LoginInput, RegisterInput, StudentInput, StudentResponse, TokenResponse, UserPublic

app = FastAPI(
    title="Student Record Manager API",
    description="Student CRUD API with JWT authentication and basic role-based access.",
    version="4.0.0",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Return readable, field-specific messages for invalid request data."""
    errors = []
    for item in exc.errors():
        location = [str(part) for part in item.get("loc", []) if part not in ("body", "query", "path")]
        field = ".".join(location) or "request"
        message = str(item.get("msg", "Invalid value")).replace("Value error, ", "")
        errors.append({"field": field, "message": message})

    return JSONResponse(
        status_code=422,
        content={
            "detail": "Please check the submitted information.",
            "errors": errors,
        },
    )


@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    """Keep database internals and credentials out of client-facing responses."""
    return JSONResponse(
        status_code=500,
        content={
            "detail": "A database error occurred. Please try again. If the problem continues, contact support."
        },
    )




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)



SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
if not SECRET_KEY or SECRET_KEY == "replace-this-with-a-long-random-secret":
    SECRET_KEY = "LOCAL-ONLY-CHANGE-ME-USE-A-RANDOM-SECRET"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))


ADMIN_EMAILS = {e.strip().lower() for e in os.getenv("ADMIN_EMAILS", "").split(",") if e.strip()}
password_hasher = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)
DbSession = Annotated[Session, Depends(get_db)]


def public_user(user: User) -> UserPublic:
    return UserPublic(id=user.id, name=user.name, email=user.email, role=user.role)


def create_access_token(user: User) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user.id), "email": user.email, "role": user.role,
        "iat": now, "exp": now + timedelta(minutes=TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    db: DbSession,
) -> User:
    if credentials is None:
        raise HTTPException(status_code=401, detail="Authentication required. Please log in.", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM], options={"require": ["exp", "sub"]})
        user_id = int(payload["sub"])
    except (InvalidTokenError, ValueError, TypeError, KeyError):
        raise HTTPException(status_code=401, detail="Invalid or expired access token. Please log in again.", headers={"WWW-Authenticate": "Bearer"})
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="User account was not found. Please log in again.", headers={"WWW-Authenticate": "Bearer"})
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def require_roles(*roles: str):
    def role_checker(user: CurrentUser) -> User:
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="You do not have permission to access this resource.")
        return user
    return role_checker


@app.on_event("startup")
def initialize_database():
    Base.metadata.create_all(bind=engine)
    # Add the role column to an existing users table if this is an older local database.
    if "users" in inspect(engine).get_table_names():
        columns = {col["name"] for col in inspect(engine).get_columns("users")}
        if "role" not in columns:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE users ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'user'"))
    if ADMIN_EMAILS:
        from sqlalchemy import select
        db = next(get_db())
        try:
            for email in ADMIN_EMAILS:
                user = db.scalar(select(User).where(func.lower(User.email) == email))
                if user and user.role != "admin":
                    user.role = "admin"
            db.commit()
        finally:
            db.close()


@app.get("/")
def home():
    return {"project": "Student Record Manager", "version": app.version, "docs": "/docs"}


@app.get("/health")
def health_check(db: DbSession):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}


@app.post("/auth/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterInput, db: DbSession):
    email = str(data.email).strip().lower()
    if db.query(User).filter(func.lower(User.email) == email).first():
        raise HTTPException(status_code=409, detail="An account with this email already exists.")
    # Role is not accepted from the request body; users cannot self-promote.
    user = User(
        name=data.name.strip(), email=email,
        hashed_password=password_hasher.hash(data.password),
        role="admin" if email in ADMIN_EMAILS else "user",
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="An account with this email already exists.")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Unable to create the account right now. Please try again.")

    return TokenResponse(access_token=create_access_token(user), user=public_user(user))


@app.post("/auth/login", response_model=TokenResponse)
def login(data: LoginInput, db: DbSession):
    email = str(data.email).strip().lower()
    user = db.query(User).filter(func.lower(User.email) == email).first()
    if not user or not password_hasher.verify(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password.", headers={"WWW-Authenticate": "Bearer"})
    return TokenResponse(access_token=create_access_token(user), user=public_user(user))


@app.post("/auth/logout")
def logout(current_user: CurrentUser):
    # JWTs are stateless; client logout removes the token. This route confirms the token was valid.
    return {"message": "Signed out successfully. Discard the access token on the client."}


@app.get("/auth/me", response_model=UserPublic)
def get_me(current_user: CurrentUser):
    return public_user(current_user)


@app.get("/admin/users", response_model=list[UserPublic])
def list_users(db: DbSession, admin: Annotated[User, Depends(require_roles("admin"))]):
    return db.query(User).order_by(User.id.asc()).all()


@app.get("/stats")
def get_dashboard_stats(db: DbSession, current_user: CurrentUser):
    owned = db.query(Student).filter(Student.owner_id == current_user.id).all()
    courses = {s.course.strip().lower() for s in owned}
    ages = [s.age for s in owned]
    return {"total_students": len(owned), "total_courses": len(courses), "average_age": round(sum(ages)/len(ages), 1) if ages else 0}




@app.get("/students", response_model=list[StudentResponse])
def get_students(
    db: DbSession,
    current_user: CurrentUser,
    q: str = Query(default="", max_length=100, description="Search by name, course, email, or ID"),
):
    query = db.query(Student).filter(
        Student.owner_id == current_user.id
    )

    term = q.strip()

    if term:
        like = f"%{term}%"
        conds = [
            Student.name.ilike(like),
            Student.course.ilike(like),
            Student.email.ilike(like),
        ]

        if term.isdigit():
            conds.append(Student.id == int(term))

        query = query.filter(or_(*conds))

    return query.order_by(Student.id.desc()).all()






@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: Annotated[int, Path(gt=0)], db: DbSession, current_user: CurrentUser):
    """Return one student owned by the authenticated user."""
    student = db.query(Student).filter(
        Student.id == student_id,
        Student.owner_id == current_user.id,
    ).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentInput, db: DbSession, current_user: CurrentUser):
    student = Student(**data.model_dump(), owner_id=current_user.id)
    db.add(student)
    try:
        db.commit()
        db.refresh(student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A conflicting student record could not be saved.")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Unable to save the student right now. Please try again.")
    return student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: Annotated[int, Path(gt=0)], data: StudentInput, db: DbSession, current_user: CurrentUser):
    student = db.query(Student).filter(Student.id == student_id, Student.owner_id == current_user.id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in data.model_dump().items():
        setattr(student, key, value)
    try:
        db.commit()
        db.refresh(student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="The updated student record conflicts with existing data.")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Unable to update the student right now. Please try again.")
    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: Annotated[int, Path(gt=0)], db: DbSession, current_user: CurrentUser):
    student = db.query(Student).filter(Student.id == student_id, Student.owner_id == current_user.id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Unable to delete the student right now. Please try again.")
    return {"message": "Student deleted successfully", "id": student_id}
