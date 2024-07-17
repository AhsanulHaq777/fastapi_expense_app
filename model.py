from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for Many-to-Many relationship between Expense and Tag
expense_tag_association = Table(
    'expense_tag_association',
    Base.metadata,
    Column('expense_id', ForeignKey('expenses.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    expenses = relationship("Expense", back_populates="owner")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    expenses = relationship("Expense", back_populates="category")

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    expenses = relationship("Expense", secondary=expense_tag_association, back_populates="tags")

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    description = Column(String)
    amount = Column(Float)
    owner_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    owner = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
    tags = relationship("Tag", secondary=expense_tag_association, back_populates="expenses")

class ExpenseTag(Base):
    __tablename__ = 'expense_tag'

    expense_id = Column(Integer, ForeignKey('expenses.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    expense = relationship("Expense", back_populates="expense_tags")
    tag = relationship("Tag", back_populates="expense_tags")
