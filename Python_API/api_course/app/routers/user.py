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
from .. database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .. import schemas
from app import utils
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/usercreate", status_code= status.HTTP_201_CREATED, response_model = schemas.UserResponse)
def user_posts(post: schemas.UserCreate, db: Session = Depends(get_db)):
    # cursor.execute("INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *",(post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    post.password = utils.hash(post.password)
    new_user = models.User(**post.dict())
    db.add(new_user)
    db.commit()
    return new_user

@router.get('/users/{id}',status_code= status.HTTP_200_OK, response_model=schemas.UserResponse)
def user_get(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail= f"The requested {id} was not found")
    db.commit()
    return user