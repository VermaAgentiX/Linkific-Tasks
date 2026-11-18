from datetime import date as Date
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    Index,
    Date as SQLDate,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Category(TimestampMixin, Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    kind: Mapped[str] = mapped_column(String(20), default="expense")
    color: Mapped[str] = mapped_column(String(7), default="#64748b")
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="category")


class Transaction(TimestampMixin, Base):
    __tablename__ = "transactions"
    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_transaction_amount_positive"),
        Index("ix_transactions_date_type", "date", "type"),
        Index("ix_transactions_category_date", "category_id", "date"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(160), index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    type: Mapped[str] = mapped_column(String(20), index=True)
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"), nullable=True
    )
    date: Mapped[Date] = mapped_column(SQLDate, default=Date.today, index=True)
    payment_method: Mapped[str] = mapped_column(String(40), default="other")
    account: Mapped[str] = mapped_column(String(80), default="Main account")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    category: Mapped[Category | None] = relationship(back_populates="transactions")


class Customer(TimestampMixin, Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    email: Mapped[str | None] = mapped_column(String(160), nullable=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class Supplier(TimestampMixin, Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    email: Mapped[str | None] = mapped_column(String(160), nullable=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class Budget(TimestampMixin, Base):
    __tablename__ = "budgets"
    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_budget_amount_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    period: Mapped[str] = mapped_column(String(20), default="monthly")
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"), nullable=True
    )
    start_date: Mapped[Date] = mapped_column(SQLDate)
    end_date: Mapped[Date | None] = mapped_column(SQLDate, nullable=True)
