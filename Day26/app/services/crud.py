from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session


def list_items(db: Session, model, skip: int = 0, limit: int = 100):
    return list(db.scalars(select(model).offset(skip).limit(limit)).all())


def get_item(db: Session, model, item_id: int):
    obj = db.get(model, item_id)
    if obj is None:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return obj


def _commit_or_raise(db: Session):
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="A unique value conflicts or a referenced record does not exist.") from exc
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail="A database error occurred. Check backend logs.") from exc


def create_item(db: Session, model, data: dict):
    obj = model(**data)
    db.add(obj)
    _commit_or_raise(db)
    db.refresh(obj)
    return obj


def update_item(db: Session, obj, data: dict):
    for key, value in data.items():
        setattr(obj, key, value)
    _commit_or_raise(db)
    db.refresh(obj)
    return obj


def delete_item(db: Session, obj):
    db.delete(obj)
    _commit_or_raise(db)
