from __future__ import annotations

from datetime import date as Date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# Categories
class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    kind: Literal["income", "expense", "both"] = "expense"
    color: str = Field(default="#64748b", pattern=r"^#[0-9A-Fa-f]{6}$")


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=80)
    kind: Literal["income", "expense", "both"] | None = None
    color: str | None = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")


class CategoryOut(ORMModel):
    id: int
    name: str
    kind: str
    color: str
    created_at: datetime
    updated_at: datetime


# Transactions
class TransactionCreate(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    amount: Decimal = Field(gt=0, max_digits=14, decimal_places=2)
    type: Literal["income", "expense"]
    category_id: int | None = None
    date: Date
    payment_method: str = Field(default="other", max_length=40)
    account: str = Field(default="Main account", max_length=80)
    notes: str | None = Field(default=None, max_length=2000)


class TransactionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=160)
    amount: Decimal | None = Field(default=None, gt=0, max_digits=14, decimal_places=2)
    type: Literal["income", "expense"] | None = None
    category_id: int | None = None
    date: Date | None = None
    payment_method: str | None = Field(default=None, max_length=40)
    account: str | None = Field(default=None, max_length=80)
    notes: str | None = Field(default=None, max_length=2000)


class TransactionOut(ORMModel):
    id: int
    title: str
    amount: Decimal
    type: str
    category_id: int | None
    date: Date
    payment_method: str
    account: str
    notes: str | None
    created_at: datetime
    updated_at: datetime


# Customers and suppliers
class ContactCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    phone: str | None = Field(default=None, max_length=30)
    email: EmailStr | None = None
    address: str | None = Field(default=None, max_length=1000)
    notes: str | None = Field(default=None, max_length=2000)

    @field_validator("email", mode="before")
    @classmethod
    def blank_email_to_none(cls, value):
        return None if value == "" else value


class ContactUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    phone: str | None = Field(default=None, max_length=30)
    email: EmailStr | None = None
    address: str | None = Field(default=None, max_length=1000)
    notes: str | None = Field(default=None, max_length=2000)

    @field_validator("email", mode="before")
    @classmethod
    def blank_email_to_none(cls, value):
        return None if value == "" else value


class ContactOut(ORMModel):
    id: int
    name: str
    phone: str | None
    email: str | None
    address: str | None
    notes: str | None
    created_at: datetime
    updated_at: datetime


# Budgets
class BudgetCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    amount: Decimal = Field(gt=0, max_digits=14, decimal_places=2)
    period: Literal["weekly", "monthly", "yearly"] = "monthly"
    category_id: int | None = None
    start_date: Date
    end_date: Date | None = None

    @model_validator(mode="after")
    def validate_date_range(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date")
        return self


class BudgetUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    amount: Decimal | None = Field(default=None, gt=0, max_digits=14, decimal_places=2)
    period: Literal["weekly", "monthly", "yearly"] | None = None
    category_id: int | None = None
    start_date: Date | None = None
    end_date: Date | None = None

    @model_validator(mode="after")
    def validate_date_range(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date")
        return self


class BudgetOut(ORMModel):
    id: int
    name: str
    amount: Decimal
    period: str
    category_id: int | None
    start_date: Date
    end_date: Date | None
    created_at: datetime
    updated_at: datetime
