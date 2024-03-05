from ast import Str
from turtle import title
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from config import Base

class Book(Base):
    __tablename__='book'

    id=Column(Integer, primary_key=True)
    title=Column(String)
    description=Column(String)
    