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

@router.get("/")
def read_root():
    return {"message": "Welcome to my world people!!!"}

@router.get("/posts",response_model = List[schemas.PostResponse])
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return posts

"""@router.post("/createposts")
def create_posts(payload:dict = Body(...)):
    print(payload)
    return {"newpost":f"title = {payload['title']},content = {payload['content']}"} """

@router.post("/posts", status_code= status.HTTP_201_CREATED, response_model = schemas.PostResponse)
def create_posts(post: schemas.PostCreate): #db: Session = Depends(get_db)
    cursor.execute("INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    # new_post = models.Post(**post.dict())
    # db.add(new_post)
    # db.commit()
    # db.refresh(new_post)
    return new_post

@router.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return post

@router.get("/posts/{id}")
def get_post(id: int,db : Session = Depends(get_db)):
  #  cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
  #  fetched_post = cursor.fetchone()
    fetched_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not fetched_post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"post with id {id} was not found")

    return fetched_post

#Deleting a post 
@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)
  #  cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *",(str(id),))
  #  deleted_post = cursor.fetchone()
  #  conn.commit()

    if not deleted_post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail= f"post with id {id} was not found")
    
    deleted_post.delete(synchronize_session = False)
    db.commit()
    # return 
    # for index,p in enumerate(my_posts):
    #     if p["id"] == id:
    #         del my_posts[index]
    #         return Response(status_code=status.HTTP_204_NO_CONTENT)
        
#Updating post 
@router.put("/posts/{id_1}", status_code = status.HTTP_200_OK, response_model = schemas.PostResponse)
def update_post(id_1: int, updated_post: schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts title = %s,content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    #index = find_index(id)
    update_post = db.query(models.Post).filter(models.Post.id == id_1)
    update_post_response = update_post.first()

    if update_post_response == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"post with id {id_1} does not exist")

    update_post.update(updated_post.dict(),synchronize_session = False)
    db.commit()
    # client_post = post.dict()
    # client_post["id"] = id
    # my_posts[index] = client_post
    return update_post
        #for p in my_posts:
    #    if p["id"] == id:

@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts