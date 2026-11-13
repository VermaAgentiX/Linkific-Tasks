from typing import Type
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Category, Transaction, Customer, Supplier, Budget
from app.schemas.resources import (
    CategoryCreate, CategoryUpdate, CategoryOut,
    TransactionCreate, TransactionUpdate, TransactionOut,
    ContactCreate, ContactUpdate, ContactOut,
    BudgetCreate, BudgetUpdate, BudgetOut
)
from app.services.crud import list_items, get_item, create_item, update_item, delete_item

router = APIRouter()

def make_crud_routes(path: str, model: Type, create_schema, update_schema, out_schema, tag: str):
    sub = APIRouter(prefix=f"/{path}", tags=[tag])

    @sub.get("", response_model=list[out_schema])
    def read_many(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=500), db: Session = Depends(get_db)):
        return list_items(db, model, skip, limit)

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

# Search route is registered before the /{item_id} route to avoid path conflicts.
search_router = APIRouter(prefix="/transactions", tags=["Transactions"])
@search_router.get("/search", response_model=list[TransactionOut])
def search_transactions(q: str = Query(min_length=1, max_length=100), db: Session = Depends(get_db)):
    return list(db.scalars(select(Transaction).where(Transaction.title.ilike(f"%{q}%")).limit(100)).all())

router.include_router(search_router)
router.include_router(make_crud_routes("categories", Category, CategoryCreate, CategoryUpdate, CategoryOut, "Categories"))
router.include_router(make_crud_routes("transactions", Transaction, TransactionCreate, TransactionUpdate, TransactionOut, "Transactions"))
router.include_router(make_crud_routes("customers", Customer, ContactCreate, ContactUpdate, ContactOut, "Customers"))
router.include_router(make_crud_routes("suppliers", Supplier, ContactCreate, ContactUpdate, ContactOut, "Suppliers"))
router.include_router(make_crud_routes("budgets", Budget, BudgetCreate, BudgetUpdate, BudgetOut, "Budgets"))
