from datetime import date as Date
from typing import Type

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Budget, Category, Customer, Supplier, Transaction
from app.schemas.resources import (
    BudgetCreate, BudgetOut, BudgetUpdate,
    CategoryCreate, CategoryOut, CategoryUpdate,
    ContactCreate, ContactOut, ContactUpdate,
    TransactionCreate, TransactionOut, TransactionUpdate,
)
from app.services.crud import create_item, delete_item, get_item, list_items, update_item


def make_crud_routes(path: str, model: Type, create_schema: Type,
                     update_schema: Type, out_schema: Type, tag: str):
    sub = APIRouter(prefix=f"/{path}", tags=[tag])

    @sub.get("", response_model=list[out_schema])
    def read_many(
        skip: int = Query(default=0, ge=0),
        limit: int = Query(default=100, ge=1, le=500),
        q: str | None = Query(default=None, min_length=1, max_length=100),
        tx_type: str | None = Query(default=None, alias="type", pattern="^(income|expense)$"),
        start_date: Date | None = None,
        end_date: Date | None = None,
        sort: str = Query(default="newest", pattern="^(newest|oldest|amount_high|amount_low|name)$"),
        db: Session = Depends(get_db),
    ):
        if model is not Transaction:
            return list_items(db, model, skip, limit)
        if start_date and end_date and end_date < start_date:
            raise HTTPException(status_code=422, detail="end_date must be on or after start_date")
        stmt = select(Transaction)
        if q:
            pattern = f"%{q.strip()}%"
            stmt = stmt.where(or_(
                Transaction.title.ilike(pattern),
                Transaction.account.ilike(pattern),
                Transaction.payment_method.ilike(pattern),
            ))
        if tx_type:
            stmt = stmt.where(Transaction.type == tx_type)
        if start_date:
            stmt = stmt.where(Transaction.date >= start_date)
        if end_date:
            stmt = stmt.where(Transaction.date <= end_date)
        order = {
            "newest": Transaction.date.desc(),
            "oldest": Transaction.date.asc(),
            "amount_high": Transaction.amount.desc(),
            "amount_low": Transaction.amount.asc(),
            "name": Transaction.title.asc(),
        }[sort]
        stmt = stmt.order_by(order, Transaction.id.desc()).offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    @sub.post("", response_model=out_schema, status_code=201)
    def create(payload: create_schema, db: Session = Depends(get_db)):
        return create_item(db, model, payload.model_dump())

    @sub.get("/{item_id}", response_model=out_schema)
    def read_one(item_id: int, db: Session = Depends(get_db)):
        return get_item(db, model, item_id)

    @sub.put("/{item_id}", response_model=out_schema)
    def update(item_id: int, payload: update_schema, db: Session = Depends(get_db)):
        return update_item(db, get_item(db, model, item_id), payload.model_dump(exclude_unset=True))

    @sub.delete("/{item_id}", status_code=204)
    def delete(item_id: int, db: Session = Depends(get_db)):
        delete_item(db, get_item(db, model, item_id))
        return None

    return sub


router = APIRouter()


@router.get("/transactions/search", response_model=list[TransactionOut], tags=["Transactions"])
def search_transactions(q: str = Query(min_length=1, max_length=100), db: Session = Depends(get_db)):
    pattern = f"%{q.strip()}%"
    stmt = select(Transaction).where(or_(
        Transaction.title.ilike(pattern),
        Transaction.account.ilike(pattern),
        Transaction.payment_method.ilike(pattern),
    )).order_by(Transaction.date.desc()).limit(100)
    return list(db.scalars(stmt).all())


router.include_router(make_crud_routes("categories", Category, CategoryCreate, CategoryUpdate, CategoryOut, "Categories"))
router.include_router(make_crud_routes("transactions", Transaction, TransactionCreate, TransactionUpdate, TransactionOut, "Transactions"))
router.include_router(make_crud_routes("customers", Customer, ContactCreate, ContactUpdate, ContactOut, "Customers"))
router.include_router(make_crud_routes("suppliers", Supplier, ContactCreate, ContactUpdate, ContactOut, "Suppliers"))
router.include_router(make_crud_routes("budgets", Budget, BudgetCreate, BudgetUpdate, BudgetOut, "Budgets"))
