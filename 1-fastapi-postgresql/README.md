# Python restapi postgresql using FastAPI and virtual environments

## &#x1F6A9; Docker container and postgresql

- create postgresql container.

        ❯ docker run -d \
        --name postgres-container \
        -e POSTGRES_USER=postgres \
        -e POSTGRES_PASSWORD=postgres \
        -p 5432:5432 \
        -v /Users/powercommerce/Documents/test/docker-mount/postgres:/var/lib/postgresql/data \
        postgres:16.1

- list images and containers

        ❯ docker images

            REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
            postgres     16.1      488c2842403b   2 months ago   448MB



        ❯ docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"

            CONTAINER ID   IMAGE           STATUS         NAMES                PORTS
            c4dc90b5c528   postgres:16.1   Up 6 seconds   postgres-container   0.0.0.0:5432->5432/tcp            
            

- check IP 

        ❯ ifconfig | grep broadcast

            inet 192.168.100.225 netmask 0xffffff00 broadcast 192.168.100.255


- test connection to postgresql

        ❯ psql -h <SESUAIKAN-HOST-IP> -U postgres

            Password for user postgres: 
            psql (16.1 (Homebrew))
            Type "help" for help.

            postgres=#


- config database and stucture

    - create database.

            postgres=# CREATE DATABASE python_db;
            CREATE DATABASE

    - show databases.

            postgres=# select datname from pg_database where datname = 'python_db';
            datname  
            -----------
            python_db
            (1 row)

    - enter into db.

            postgres=# \c python_db 
            You are now connected to database "python_db" as user "postgres".    

    - create table

            python_db=# CREATE TABLE book(
            python_db(# id serial primary key,
            python_db(# title text not null,
            python_db(# description char(200)
            python_db(# );
            CREATE TABLE
            python_db=# \d
                        List of relations
            Schema |    Name     |   Type   |  Owner   
            --------+-------------+----------+----------
            public | book        | table    | postgres
            public | book_id_seq | sequence | postgres
            (2 rows)

            python_db=# CREATE TABLE library(
            python_db(# id serial primary key,
            python_db(# name text not null,
            python_db(# country text
            python_db(# );
            CREATE TABLE
            python_db=# \d
                        List of relations
            Schema |      Name      |   Type   |  Owner   
            --------+----------------+----------+----------
            public | book           | table    | postgres
            public | book_id_seq    | sequence | postgres
            public | library        | table    | postgres
            public | library_id_seq | sequence | postgres
            (4 rows)

    - quit.

            postgres=# \q
---

## &#x1F6A9; Code restapi with FastAPI

create virtual environments

    ❯ python -m venv venv


ally in the local virtual environments.

    ❯ source venv/bin/activate


install some necessary packages (test with another version of fastapi) --> SUCCESSFUL | &#x2705; RECOMMANDED VERSION

    ❯ pip install uvicorn==0.27.1 fastapi==0.99.1    

        notes : [fastapi] There is a lack of support for newer versions of fastapi, 
        so it is recommended to use this version or a level not further below it.

    ❯ pip install SQLAlchemy==2.0.28

    ❯ pip install psycopg2==2.9.9

    ❯ pip install flask==3.0.2


---

&#x1FAA7; notes : 

    ❯ pip list

        Package           Version
        ----------------- -------
        anyio             4.3.0
        blinker           1.7.0
        click             8.1.7
        exceptiongroup    1.2.0
        fastapi           0.99.1
        Flask             3.0.2
        h11               0.14.0
        idna              3.6
        itsdangerous      2.1.2
        Jinja2            3.1.3
        MarkupSafe        2.1.5
        pip               22.0.4
        psycopg2          2.9.9
        pydantic          1.10.14
        setuptools        58.1.0
        sniffio           1.3.1
        SQLAlchemy        2.0.28
        starlette         0.27.0
        typing_extensions 4.10.0
        uvicorn           0.27.1
        Werkzeug          3.0.1

build a project folder and its files.

    ❯ cd 1-fastapi-postgresql

    ❯ mkdir -p app

    ❯ cd app

    ❯ touch main.py config.py model.py schemas.py crud.py router.py 

    ❯ tree ./

        ├── config.py
        ├── crud.py
        ├── main.py
        ├── model.py
        ├── router.py
        └── schemas.py

#### &#x1F530; Code main.py : 

Basic project.

        from fastapi import FastAPI

        app=FastAPI()

        @app.get('/')
        async def Home():
            return "Welcome Home"

#### &#x1F3C4; Run project

        ❯ uvicorn main:app --reload

            INFO:     Will watch for changes in these directories: ['/Users/.../python-restAPI-postgresql-using-FastAPI-and-virtualenv/1-fastapi-postgresql/app']
            INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
            INFO:     Started reloader process [98301] using StatReload
            INFO:     Started server process [98303]
            INFO:     Waiting for application startup.
            INFO:     Application startup complete.            


<p align="center">
    <img src="./gambar-petunjuk/ss_001_fastapi-1.png" alt="ss_001_fastapi-1" style="display: block; margin: 0 auto;">
</p>
<p align="center">Main | Browser http://localhost:8000</p>

<p align="center">
    <img src="./gambar-petunjuk/ss_001_fastapi-1-swagger.png" alt="ss_001_fastapi-1-swagger" style="display: block; margin: 0 auto;">
</p>
<p align="center">Swagger | Browser http://localhost:8000/docs</p>

---

&#x1F6A7; continue with the next code development.

#### &#x1F530; Code main.py :

    from fastapi import FastAPI

    import model
    from config import engine
    import router

    model.Base.metadata.create_all(bind=engine)

    app=FastAPI()

    @app.get('/')
    async def Home():
        return "Welcome Home | أهلاً بك في بيتك | 欢迎回家 | Добро пожаловать домой"

    app.include_router(router.router,prefix="/book",tags=["book"])



#### &#x1F530; Code config.py :

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    DATABASE_URL="postgresql://postgres:postgres@192.168.100.225:5432/python_db"

    engine=create_engine(DATABASE_URL)
    SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
    Base=declarative_base()



#### &#x1F530; Code model.py :

    from sqlalchemy import Column, Integer, String
    from config import Base

    class Book(Base):
        __tablename__='book'

        id=Column(Integer, primary_key=True)
        title=Column(String)
        description=Column(String)
    
        

#### &#x1F530; Code schemas.py :

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

    class Response(GenericModel, Generic[T]):
        code: str
        status: str
        message: str
        result: Optional[T]




#### &#x1F530; Code crud.py :

    from sqlalchemy.orm import Session
    from model import Book
    from schemas import BookSchema

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




#### &#x1F530; Code routes.py :

    from fastapi import APIRouter, HTTPException, Path, Depends
    from config import SessionLocal
    from sqlalchemy.orm import Session
    from schemas import BookSchema,RequestBook,Response
    import crud

    router=APIRouter()

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
    
    


---

#### &#x1F3C4; Run project

Here are the results of running the project if using the latest version or from a non-recommended version of fastapi

        ❯ uvicorn main:app --reload

            INFO:     Will watch for changes in these directories: ['/Users/.../python-restAPI-postgresql-using-FastAPI-and-virtual-environments/1-fastapi-postgresql/app']
            INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
            INFO:     Started reloader process [14386] using StatReload
            /Users/.../python-restAPI-postgresql-using-FastAPI-and-virtual-environments/venv/lib/python3.10/site-packages/pydantic/_migration.py:283: UserWarning: `pydantic.generics:GenericModel` has been moved to `pydantic.BaseModel`.
            warnings.warn(f'`{import_path}` has been moved to `{new_location}`.')
            /Users/.../python-restAPI-postgresql-using-FastAPI-and-virtual-environments/venv/lib/python3.10/site-packages/pydantic/_internal/_config.py:322: UserWarning: Valid config keys have changed in V2:
            * 'orm_mode' has been renamed to 'from_attributes'
            warnings.warn(message, UserWarning)
            INFO:     Started server process [14388]
            INFO:     Waiting for application startup.
            INFO:     Application startup complete.

---

Here are the results of running the project if using the recommended version of fastapi &#x2705; .

        ❯ uvicorn main:app --reload

            INFO:     Will watch for changes in these directories: ['/Users/.../python-restAPI-postgresql-using-FastAPI-and-virtual-environments/1-fastapi-postgresql/app']
            INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
            INFO:     Started reloader process [95230] using StatReload
            INFO:     Started server process [95232]
            INFO:     Waiting for application startup.
            INFO:     Application startup complete.

&#x1FAA7; notes :

If you encounter the following error while running the project, deactivate the virtual environment and access the venv/bin/activate source again.

    . . .
    ModuleNotFoundError: No module named 'sqlalchemy'

---





### &#x1F31F; CURL : 

- &#x1F536; book [create book]

        curl --location 'http://localhost:8000/book/create' \
        --header 'Content-Type: application/json' \
        --data '{
            "parameter":{
                "title":"The Book of War",
                "description": "Two classic works of military strategy that shaped the way we think about warfare"
            }
        }'

- &#x1F536; book [get all book]

        curl --location 'http://localhost:8000/book/'


- &#x1F536; book [get by id book]

        curl --location 'http://localhost:8000/book/35'

- &#x1F536; book [update book]

        curl --location --request PATCH 'http://localhost:8000/book/update' \
        --header 'Content-Type: application/json' \
        --data '{
            "parameter":{
                "id": 35,
                "title":"The Book of War 2",
                "description": "Two classic works of military strategy that shaped the way we think about warfare"
            }
        }'

- &#x1F536; book [delete book]

        curl --location --request DELETE 'http://localhost:8000/book/35'




---


<p align="center">
    <img src="./gambar-petunjuk/ss_001_fastapi-book-swagger.png" alt="ss_001_fastapi-book-swagger" style="display: block; margin: 0 auto;">
</p>
<p align="center">Swagger | Browser http://localhost:8000/docs</p>