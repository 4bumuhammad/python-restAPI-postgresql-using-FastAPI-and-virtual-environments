#from dbm.ndbm import library
#import imp
from turtle import title
from flask import session
from sqlalchemy.orm import Session

from model import Book
from model import Library

from schemas import BookSchema
from schemas import LibrarySchema

# Get All book data
def get_book(db:Session,skip:int=0,limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all()

# Get by id book data
def get_book_by_id(db:Session,book_id:int):
    return db.query(Book).filter(Book.id==book_id).first()

# Create book data
def create_book(db:Session,book: BookSchema):
    _book=Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

# Remove book data
def remove_book(db:Session,book_id:int):
    _book=get_book_by_id(db=db,book_id=book_id)
    db.delete(_book)
    db.commit()

# Update book data
def update_book(db:Session,book_id:int,title:str,description:str):
    _book=get_book_by_id(db=db,book_id=book_id)
    _book.title=title
    _book.description=description
    db.commit()
    db.refresh(_book)
    return _book



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Get All library data
def get_library(db:Session,skip:int=0,limit:int=100):
    return db.query(Library).offset(skip).limit(limit).all()

# Get by id library data
def get_library_by_id(db:Session,library_id:int):
    return db.query(Library).filter(Library.id==library_id).first()

# Create library data
def create_library(db:Session,library: LibrarySchema):
    _library=Library(name=library.name,country=library.country)
    db.add(_library)
    db.commit()
    db.refresh(_library)
    return _library

# Remove library data
def remove_library(db:Session,library_id:int):
    _library=get_library_by_id(db=db,library_id=library_id)
    db.delete(_library)
    db.commit()

# Update library data
def update_library(db:Session, library_id:int,name:str,country:str):
    _library=get_library_by_id(db=db,library_id=library_id)
    _library.name=name
    _library.country=country
    db.commit()
    db.refresh(_library)
    return _library