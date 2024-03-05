from inspect import Parameter
from optparse import Option
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel

T=TypeVar('T')

class BookSchema(BaseModel):
    id:Optional[int]=None
    title:Optional[str]=None
    description:Optional[str]=None

    class Config:
        orm_mode=True

class RequestBook(BaseModel):
    parameter: BookSchema=Field(...)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class LibrarySchema(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None
    country:Optional[str]=None

    class Config:
        orm_mode=True

class RequestLibrary(BaseModel):
    parameter: LibrarySchema=Field(...)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

