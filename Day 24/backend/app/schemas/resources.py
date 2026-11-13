from datetime import date, datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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

class TransactionCreate(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    amount: Decimal = Field(gt=0, max_digits=14, decimal_places=2)
    type: Literal["income", "expense"]
    category_id: int | None = None
    date: date
    payment_method: str = Field(default="other", max_length=40)
    account: str = Field(default="Main account", max_length=80)
    notes: str | None = Field(default=None, max_length=2000)
class TransactionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=160)
    amount: Decimal | None = Field(default=None, gt=0, max_digits=14, decimal_places=2)
    type: Literal["income", "expense"] | None = None
    category_id: int | None = None
    date: date | None = None
    payment_method: str | None = Field(default=None, max_length=40)
    account: str | None = Field(default=None, max_length=80)
    notes: str | None = Field(default=None, max_length=2000)
class TransactionOut(ORMModel):
    id: int
    title: str
    amount: Decimal
    type: str
    category_id: int | None
    date: date
    payment_method: str
    account: str
    notes: str | None
    created_at: datetime
    updated_at: datetime

class ContactCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    phone: str | None = Field(default=None, max_length=30)
    email: str | None = Field(default=None, max_length=160)
    address: str | None = Field(default=None, max_length=1000)
    notes: str | None = Field(default=None, max_length=2000)
class ContactUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    phone: str | None = Field(default=None, max_length=30)
    email: str | None = Field(default=None, max_length=160)
    address: str | None = Field(default=None, max_length=1000)
    notes: str | None = Field(default=None, max_length=2000)
class ContactOut(ORMModel):
    id: int
    name: str
    phone: str | None
    email: str | None
    address: str | None
    notes: str | None
    created_at: datetime
    updated_at: datetime

class BudgetCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    amount: Decimal = Field(gt=0, max_digits=14, decimal_places=2)
    period: Literal["weekly", "monthly", "yearly"] = "monthly"
    category_id: int | None = None
    start_date: date
    end_date: date | None = None
class BudgetUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    amount: Decimal | None = Field(default=None, gt=0, max_digits=14, decimal_places=2)
    period: Literal["weekly", "monthly", "yearly"] | None = None
    category_id: int | None = None
    start_date: date | None = None
    end_date: date | None = None
class BudgetOut(ORMModel):
    id: int
    name: str
    amount: Decimal
    period: str
    category_id: int | None
    start_date: date
    end_date: date | None
    created_at: datetime
    updated_at: datetime
