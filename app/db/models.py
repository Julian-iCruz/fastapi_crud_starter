import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(100), index=True)
    description = Column(String(255), nullable=True)
    quantity = Column(Integer, default=0)
    cost = Column(Float, default=0.0)
    status = Column(String(50), default="active")
