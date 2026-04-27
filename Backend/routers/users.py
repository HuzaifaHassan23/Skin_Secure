from typing import Annotated, cast

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Import local files
import database
import models
import schemas
from Security.hashing import get_password_hash, verify_password
from Security.dependencies import get_current_user

router = APIRouter(prefix="/user", tags=["profile"])


@router.put("/profile")
async def update_profile(
    update_data: schemas.UserUpdate,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[Session, Depends(database.get_db)]
):
    """Update user profile information (name, age, email, language). Requires valid JWT token."""
    
    # Get the current user from database
    user = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if email is being changed and if it's already taken
    if update_data.email and update_data.email != user.email:
        existing_email = db.query(models.User).filter(models.User.email == update_data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email is already in use")
    
    # Update only provided fields
    if update_data.name is not None:
        user.name = update_data.name
    if update_data.email is not None:
        user.email = update_data.email
    if update_data.age is not None:
        user.age = update_data.age
    if update_data.preferred_language is not None:
        user.preferred_language = update_data.preferred_language
    
    # Save changes
    db.commit()
    db.refresh(user)
    
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "preferred_language": user.preferred_language
    }


@router.put("/password")
async def change_password(
    password_data: schemas.PasswordUpdate,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[Session, Depends(database.get_db)]
):
    """Change user password. Requires valid JWT token and correct current password."""
    
    # Get the current user from database
    user = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verify current password
    if not verify_password(password_data.current_password, cast(str, user.hashed_password)):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    
    # Validate new password length
    if len(password_data.new_password) < 6:
        raise HTTPException(status_code=400, detail="New password must be at least 6 characters")
    
    # Hash and save new password
    user.hashed_password = get_password_hash(password_data.new_password)
    db.commit()
    
    return {"message": "Password updated successfully"}
