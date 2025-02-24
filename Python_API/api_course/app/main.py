from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import enum 
import psycopg2 # type: ignore
from psycopg2.extras import RealDictCursor #type: ignore
import time
from . import models
#from models import Post
from .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from . import schemas
from app import utils
from routers import post
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
                   

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password='skapeed24!)97', cursor_factory=RealDictCursor)   
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error",error)
        time.sleep(2)

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index(id):
    for index,p in enumerate(my_posts):
        if p["id"] == id:
            return index

app = FastAPI()





        


