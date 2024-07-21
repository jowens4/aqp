from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl
from fastapi import UploadFile, File


class DogboneCreate(BaseModel):
    timestamp: Optional[datetime]
    number: str
    note: str
    length: str
    width: str
    thickness: str
    file_name: str
    file_data: str

class Dogbone(DogboneCreate):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
