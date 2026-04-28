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

    # Relationships
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    scans = relationship("Scan", back_populates="user", cascade="all, delete-orphan")

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

class Scan(Base):
    __tablename__ = "scans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    body_part: Mapped[str] = mapped_column(String(100))
    symptoms: Mapped[str] = mapped_column(Text) # Stored as "Itching, Redness"
    
    primary_prediction: Mapped[str] = mapped_column(String(100))
    confidence: Mapped[float] = mapped_column()
    risk_level: Mapped[str] = mapped_column(String(20)) # "high", "med", "low"
    
    # Store file paths, not the actual images!
    raw_image_path: Mapped[str] = mapped_column(String(255))
    heatmap_path: Mapped[str] = mapped_column(String(255))
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship("User", back_populates="scans")