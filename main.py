from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favourite foods","content":"I like pizza","id":2}]

def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/posts")
def get_posts():
    return{"data":my_posts}
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/posts") 
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data":post_dict}
   

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_posts(id)
    print(post)
    return{"post_detail": post}