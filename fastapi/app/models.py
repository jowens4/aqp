from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary # Import DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from fastapi import UploadFile



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Dogbone(Base):
    __tablename__ = "dogbones"
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    number = Column(String, index=True)
    note = Column(String, index=True)
    length = Column(String)
    width = Column(String)
    thickness = Column(String)
    file_name = Column(String)
    file_data = Column(String)