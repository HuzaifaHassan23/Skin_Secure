from typing import Annotated, cast

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Import local files
import database
import models
import schemas
from Security.hashing import get_password_hash, verify_password
from Security.jwt_tokens import create_access_token
from Security.dependencies import get_current_user

router = APIRouter()


# Registration Endpoint
@router.post("/register")
def register_user(user: schemas.UserCreate, db: Annotated[Session, Depends(database.get_db)]):
    # Check if a user with this email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    # Hash the password securely
    hashed_pw = get_password_hash(user.password)
    
    # Create the new user object mapped to the database model
    new_user = models.User(
        name=user.name,
        email=user.email,
        age=user.age,
        preferred_language=user.preferred_language,
        hashed_password=hashed_pw  # IMPORTANT: Save the hash, NEVER the plain password!
    )
    
    # Save to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # Retrieves the newly generated ID from MySQL
    
    # Create JWT token
    token = create_access_token(user_id=new_user.id, name=new_user.name, email=new_user.email)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "age": new_user.age,
            "preferred_language": new_user.preferred_language
        }
    }

# Login Endpoint 
@router.post("/login")
async def login_user(credentials: schemas.UserLogin, db: Annotated[Session, Depends(database.get_db)]):  
    # Find the user by email
    db_user = db.query(models.User).filter(models.User.email == credentials.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Verify the password
    if not verify_password(credentials.password, cast(str, db_user.hashed_password)):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Create JWT token
    token = create_access_token(user_id=db_user.id, name=db_user.name, email=db_user.email)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "age": db_user.age,
            "preferred_language": db_user.preferred_language
        }
    }


# Protected Endpoint - Get User Profile
@router.get("/user/profile")
async def get_profile(current_user: Annotated[dict, Depends(get_current_user)], db: Annotated[Session, Depends(database.get_db)]):
    """Get the current user's profile. Requires valid JWT token."""
    # current_user contains: {user_id, name, email, exp}
    user = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "preferred_language": user.preferred_language
    }
