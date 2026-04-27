from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

# Import local files
import database
import models
import schemas
from Security.dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["community"])


@router.post("", response_model=schemas.PostResponse)
async def create_post(
    post_data: schemas.PostCreate,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[Session, Depends(database.get_db)]
):
    """Create a new post in the community."""
    
    new_post = models.Post(
        author_id=current_user["user_id"],
        post_title=post_data.post_title,
        body=post_data.body,
        type_of_post=post_data.type_of_post,
        is_anonymous=post_data.is_anonymous, # <--- SAVE IT TO DB
        likes=0
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    # Get author name
    author = db.query(models.User).filter(models.User.id == new_post.author_id).first()
    
    # --- ANONYMOUS LOGIC ---
    if new_post.is_anonymous:
        author_name = "Anonymous"
    else:
        author_name = author.name if author else "Unknown"
    
    comment_count = len(new_post.comments)
    return {
        "id": new_post.id,
        "author_id": new_post.author_id,
        "author_name": author_name,
        "is_anonymous": new_post.is_anonymous,
        "post_title": new_post.post_title,
        "body": new_post.body,
        "type_of_post": new_post.type_of_post,
        "likes": new_post.likes,
        "created_at": new_post.created_at,
        "comment_count": comment_count
    }


@router.get("", response_model=List[schemas.PostResponse])
async def get_all_posts(
    db: Annotated[Session, Depends(database.get_db)]
):
    """Get all posts ordered by newest first."""
    
    posts = db.query(models.Post).order_by(models.Post.created_at.desc()).all()
    
    result = []
    for post in posts:
        author = db.query(models.User).filter(models.User.id == post.author_id).first()
        
        # --- ANONYMOUS LOGIC ---
        if post.is_anonymous:
            author_name = "Anonymous"
        else:
            author_name = author.name if author else "Unknown"
            
        comment_count = len(post.comments)
        result.append({
            "id": post.id,
            "author_id": post.author_id,
            "author_name": author_name,
            "is_anonymous": post.is_anonymous,
            "post_title": post.post_title,
            "body": post.body,
            "type_of_post": post.type_of_post,
            "likes": post.likes,
            "created_at": post.created_at,
            "comment_count": comment_count
        })
    
    return result


@router.get("/{post_id}", response_model=schemas.PostDetailResponse)
async def get_post_with_comments(
    post_id: int,
    db: Annotated[Session, Depends(database.get_db)]
):
    """Get a specific post with all its comments. Used for expanding comment section."""
    
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Get author name
    author = db.query(models.User).filter(models.User.id == post.author_id).first()
    author_name = author.name if author else "Unknown"
    
    # Map comments to response format with author names
    comments = []
    for comment in post.comments:
        comment_author = db.query(models.User).filter(models.User.id == comment.author_id).first()
        comment_author_name = comment_author.name if comment_author else "Unknown"
        comments.append({
            "id": comment.id,
            "body": comment.body,
            "author_id": comment.author_id,
            "author_name": comment_author_name,
            "created_at": comment.created_at
        })
    
    return {
        "id": post.id,
        "author_id": post.author_id,
        "author_name": author_name,
        "is_anonymous": post.is_anonymous,
        "post_title": post.post_title,
        "body": post.body,
        "type_of_post": post.type_of_post,
        "likes": post.likes,
        "created_at": post.created_at,
        "comments": comments
    }


@router.post("/{post_id}/comments", response_model=schemas.CommentResponse)
async def create_comment(
    post_id: int,
    comment_data: schemas.CommentCreate,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[Session, Depends(database.get_db)]
):
    """Create a new comment on a post. Requires valid JWT token."""
    
    # Verify post exists
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Create new comment with author_id
    new_comment = models.Comment(
        post_id=post_id,
        author_id=current_user["user_id"],
        body=comment_data.body
    )
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    # Get author name
    comment_author = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    author_name = comment_author.name if comment_author else "Unknown"
    
    return {
        "id": new_comment.id,
        "body": new_comment.body,
        "author_id": new_comment.author_id,
        "author_name": author_name,
        "created_at": new_comment.created_at
    }


@router.post("/{post_id}/like")
async def like_post(
    post_id: int,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[Session, Depends(database.get_db)]
):
    """Like a post (increment likes counter). Requires valid JWT token."""
    
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Increment likes
    post.likes += 1
    db.commit()
    db.refresh(post)
    
    return {"likes": post.likes, "message": "Post liked successfully"}
