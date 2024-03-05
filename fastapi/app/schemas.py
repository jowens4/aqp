from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi import UploadFile


class Dogbone(BaseModel):
    id: int
    timestamp: Optional[datetime]
    number: str
    note: str
    length: str
    width: str
    thickness: str
    files: str

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: str | None = None


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
    items: list[Item] = []

    class Config:
        orm_mode = True