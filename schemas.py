from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class TagBase(BaseModel):
    name: str

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    date: datetime
    description: str
    amount: float

class ExpenseCreate(ExpenseBase):
    owner_id: int
    category_id: int
    tags: Optional[List[int]] = []

class ExpenseUpdate(ExpenseBase):
    owner_id: Optional[int] = None
    category_id: Optional[int] = None
    tags: Optional[List[int]] = None

class Expense(ExpenseBase):
    id: int
    owner: User
    category: Category
    tags: List[Tag] = []

    class Config:
        orm_mode = True

class ExpenseTagBase(BaseModel):
    expense_id: int
    tag_id: int

class ExpenseTag(ExpenseTagBase):
    class Config:
        orm_mode = True
