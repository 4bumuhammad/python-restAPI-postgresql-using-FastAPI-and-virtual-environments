## Artikel
# LemonCode21 https://www.youtube.com/watch?v=d_ugoWsvGLI

$ pip3 install -U pip virtualenv
$ virtualenv --system-site-packages -p python ./venv

# Create virtual environment
$ virtualenv venv

# masuk pada virtual environment
$ source venv/bin/activate

# install beberapa package
$ pip install uvicorn fastapi

# buat folder app dan berisi file main.py
$ mkdir -p app
$ touch main.py
$ cd app

# compile test
$ uvicorn main:app --reload
op:
INFO:     Will watch for changes in these directories: ['/Users/powercommerce/Documents/Work/my-development/python/003-restAPI_usingFlask/2-fastapi-postgresql/app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7985] using statreload
INFO:     Started server process [7987]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

# catatan :
akan membuat sebuah directory __pycache__


# buat file config.py
# kemudian install package :
$ pip install sqlalchemy

# buat file model.py
# - juga setelah melakukan penambahan code pada main.py
# install package 
$ pip install psycopg2

# buat file schemas.py

# buat file crud.py

# buat file routes.py


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create DATA postgres
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

❯ psql -U postgres
psql (14.2)
Type "help" for help.

postgres=# CREATE DATABASE python_db;
CREATE DATABASE
postgres=# \l
postgres=# \c python_db
You are now connected to database "python_db" as user "postgres".
python_db=# CREATE TABLE book(
python_db(# id serial primary key,
python_db(# title text not null,
python_db(# description char(200)
python_db(# );
CREATE TABLE
python_db=# \d
        List of relations
 Schema | Name | Type  |  Owner
--------+------+-------+----------
 public | book | table | postgres
(1 row)

python_db=# CREATE TABLE library(
python_db(# id serial primary key,
python_db(# name text not null,
python_db(# country text
python_db(# );


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Test runing python with uvicorn fastapi
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
$ source venv/bin/activate
$ cd app
$ uvicorn main:app --reload