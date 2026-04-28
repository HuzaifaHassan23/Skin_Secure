from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
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
    age: int

    class Config:
        orm_mode = True # Tells Pydantic to read data from SQLAlchemy models
        from_attributes = True # Tells Pydantic to read data from SQLAlchemy models
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    """Schema for updating user profile information (all fields optional)."""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    preferred_language: Optional[int] = None

class PasswordUpdate(BaseModel):
    """Schema for changing user password."""
    current_password: str
    new_password: str

# --- POST & COMMENT SCHEMAS ---
class PostCreate(BaseModel):
    """Schema for creating a new post."""
    post_title: str
    body: str
    type_of_post: Literal["Story", "Question", "Advice"]
    is_anonymous: bool = False

class CommentCreate(BaseModel):
    """Schema for creating a new comment."""
    body: str

class AuthorInfo(BaseModel):
    """Author information for posts and comments."""
    user_id: int
    name: str

class CommentResponse(BaseModel):
    """Schema for returning a comment with author info."""
    id: int
    body: str
    author_id: int
    author_name: str  # Include author name
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True

class PostResponse(BaseModel):
    """Schema for returning a post with basic comment info."""
    id: int
    author_id: int
    author_name: str  # Include author name
    post_title: str
    body: str
    type_of_post: str
    likes: int
    created_at: datetime
    is_anonymous: bool = False
    comment_count: int = 0  # Number of comments, not full comment objects

    class Config:
        orm_mode = True
        from_attributes = True

class PostDetailResponse(BaseModel):
    """Schema for returning a post with all comments expanded."""
    id: int
    author_id: int
    author_name: str  # Include author name
    post_title: str
    body: str
    type_of_post: str
    likes: int
    created_at: datetime
    is_anonymous: bool = False
    comments: List[CommentResponse] = []

    class Config:
        orm_mode = True
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ScanResponse(BaseModel):
    id: int
    body_part: str
    symptoms: str
    primary_prediction: str
    confidence: float
    risk_level: str
    raw_image_path: str
    heatmap_path: str
    created_at: datetime

    class Config:
        from_attributes = True