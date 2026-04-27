from sqlalchemy import String, Integer, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    # Notice the type hints (Mapped[int], Mapped[str]) before the assignment!
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    
    # Use standard Python type hinting for optional/nullable fields
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    preferred_language: Mapped[int] = mapped_column(default=1) 
    hashed_password: Mapped[str] = mapped_column(String(255))

    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    post_title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(Text)
    
    type_of_post: Mapped[str] = mapped_column(Enum("Story", "Question", "Advice", name="post_types"), default="Story")
    
    # ADD THIS LINE TO SAVE THE ANONYMOUS CHOICE
    is_anonymous: Mapped[bool] = mapped_column(default=False) 
    
    likes: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    post = relationship("Post", back_populates="comments")
    author = relationship("User")