from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def get_posts():
    return{"data":"This is your posts"}
@app.get("/post")
def root():
    return {"message": "Hello World"}

@app.post("/createposts") 
def create_posts(post:Post):
    print(post)
    print(post.dict())
    return{"data":post}
   