"""Pydantic schemas with normalized input and strict request validation."""
import re
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class RegisterInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        value = " ".join(value.split())
        if len(value) < 2:
            raise ValueError("Name must contain at least 2 non-space characters.")
        if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", value):
            raise ValueError("Name can contain letters, spaces, apostrophes, periods, and hyphens only.")
        return value

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: EmailStr) -> EmailStr:
        return str(value).strip().lower()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Password cannot contain only spaces.")
        return value


class LoginInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: EmailStr) -> EmailStr:
        return str(value).strip().lower()


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: EmailStr
    role: str = "user"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic


class StudentInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=1, le=120, strict=True)
    course: str = Field(min_length=2, max_length=100)
    email: EmailStr

    @field_validator("name", "course")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        value = " ".join(value.split())
        if len(value) < 2:
            raise ValueError("Must contain at least 2 non-space characters.")
        return value

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: EmailStr) -> EmailStr:
        return str(value).strip().lower()


class StudentResponse(StudentInput):
    model_config = ConfigDict(from_attributes=True)
    id: int
