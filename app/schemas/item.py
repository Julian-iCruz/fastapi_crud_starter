from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = 0
    cost: float = 0.0


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemOut(ItemBase):
    id: UUID

    class Config:
        from_attributes = True
