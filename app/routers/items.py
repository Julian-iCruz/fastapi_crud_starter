from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import SessionLocal
from db import models
from schemas.item import ItemCreate, ItemUpdate, ItemOut

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ItemOut)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=ItemOut)
def update_item(item_id: str, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db_item.quantity = item.quantity
    db_item.cost = item.cost

    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}
