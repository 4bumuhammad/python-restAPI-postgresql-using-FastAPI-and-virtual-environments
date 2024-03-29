from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema,RequestBook,Response
from schemas import LibrarySchema, RequestLibrary, Response
import crud

router=APIRouter()
router_library=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestBook,db:Session=Depends(get_db)):
    crud.create_book(db,request.parameter)
    return Response(code=200,status="OK",message="Book created successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _book=crud.get_book(db,0,100)
    return Response(code=200,status="OK",message="Success Fetch all data",result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _book=crud.get_book_by_id(db,id)
    return Response(code=200,status="OK", message="Success get data", result=_book).dict(exclude_none=True)


@router.patch("/update")
async def update_book(request:RequestBook, db:Session=Depends(get_db)):
    _book=crud.update_book(db,book_id=request.parameter.id,title=request.parameter.title, description=request.parameter.description)
    return Response(code=200,status="OK",message="Success update data",result=_book)


@router.delete("/{id}")
async def delete(id:int,db:Session=Depends(get_db)):
    crud.remove_book(db,book_id=id)
    return Response(code=200, status="OK", message="Success delete data").dict(exclude_none=True)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@router_library.post("/create")
async def create(request:RequestLibrary,db:Session=Depends(get_db)):
    crud.create_library(db,request.parameter)
    return Response(code=200,status="OK",message="Library created successfully").dict(exclude_none=True)

@router_library.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _library=crud.get_library_by_id(db,id)
    return Response(code=200,status="OK",message="Success get data", result=_library).dict(exclude_none=True)

@router_library.get("/")
async def get(db:Session=Depends(get_db)):
    _library=crud.get_library(db,0,100)
    return Response(code=200,status="OK",message="Success Fetch all data", result=_library).dict(exclude_none=True)

@router_library.patch("/update")
async def update_library(request:RequestLibrary, db:Session=Depends(get_db)):
    _library=crud.update_library(db,library_id=request.parameter.id,name=request.parameter.name,country=request.parameter.country)
    return Response(code=200,status="OK",message="Success update data", result=_library)

@router_library.delete("/{id}")
async def delete(id:int,db:Session=Depends(get_db)):
    crud.remove_library(db,library_id=id)
    return Response(code=200,status="OK",message="Success delete data").dict(exclude_none=True)