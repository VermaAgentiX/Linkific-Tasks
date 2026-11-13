from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

def list_items(db: Session, model, skip: int = 0, limit: int = 100):
    return list(db.scalars(select(model).offset(skip).limit(limit)).all())

def get_item(db: Session, model, item_id: int):
    obj = db.get(model, item_id)
    if obj is None:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return obj

def create_item(db: Session, model, data: dict):
    obj = model(**data)
    db.add(obj)
    try:
        db.commit()
        db.refresh(obj)
    except Exception:
        db.rollback()
        raise
    return obj

def update_item(db: Session, obj, data: dict):
    for key, value in data.items():
        setattr(obj, key, value)
    try:
        db.commit()
        db.refresh(obj)
    except Exception:
        db.rollback()
        raise
    return obj

def delete_item(db: Session, obj):
    db.delete(obj)
    db.commit()
