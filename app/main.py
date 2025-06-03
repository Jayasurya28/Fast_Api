from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine
from app.routers import post, user, auth, vote
from app.config import settings

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI",
    description="FastAPI application with authentication and CRUD operations",
    version="0.1.0",
    openapi_tags=[
        {"name": "Posts", "description": "Operations with posts"},
        {"name": "Users", "description": "Operations with users"},
        {"name": "Auth", "description": "Authentication operations"},
        {"name": "Vote", "description": "Vote operations"},
    ]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, prefix="/posts", tags=["Posts"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(vote.router, prefix="/vote", tags=["Vote"])

@app.get("/", tags=["default"])
def read_root():
    return {"message": "Hi JS !!"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # Use PORT from environment, default 8080
    uvicorn.run(app, host="0.0.0.0", port=port)