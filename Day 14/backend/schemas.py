"""Pydantic request and response schemas for the FastAPI API."""
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginInput(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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


class StudentResponse(StudentInput):
    model_config = ConfigDict(from_attributes=True)

    id: int
