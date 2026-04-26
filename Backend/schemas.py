from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- USER SCHEMAS ---
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int
    preferred_language: int = 1

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    preferred_language: int

    class Config:
        orm_mode = True # Tells Pydantic to read data from SQLAlchemy models
        from_attributes = True # Tells Pydantic to read data from SQLAlchemy models
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# --- POST SCHEMAS ---
class PostCreate(BaseModel):
    post_title: str
    body: str
    type_of_post: str

class CommentResponse(BaseModel):
    id: int
    body: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    author_id: int
    post_title: str
    body: str
    type_of_post: str
    likes: int
    created_at: datetime
    
    # We can return the number of comments directly
    comments: List[CommentResponse] = []

    class Config:
        orm_mode = True
        from_attributes = True