import hashlib
from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import hashlib

# Import local files
import database
import models
import schemas

# Create the database tables automatically (if they don't exist yet)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Skin Secure API")

# Setup the Password Hashing Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hash password using SHA256 first (to handle >72 chars), then bcrypt."""
    # SHA256 ensures consistent 64-char hash regardless of password length
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    # bcrypt hash the SHA256 hash (always 64 chars, well under 72 byte limit)
    return pwd_context.hash(sha256_hash)


# Registration Endpoint
@app.post("/register", response_model=schemas.UserResponse)
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
    
    return new_user

# Login Endpoint 
@app.post("/login")
async def login_user(credentials: schemas.UserLogin, db: Annotated[Session, Depends(database.get_db)]):  
    # Find the user by email
    db_user = db.query(models.User).filter(models.User.email == credentials.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Hash the provided password and compare with stored hash
    sha256_hash = hashlib.sha256(credentials.password.encode()).hexdigest()
    stored_hash = db_user.hashed_password
    if not isinstance(stored_hash, str):
        raise HTTPException(status_code=500, detail="Stored password hash is invalid")
    if not pwd_context.verify(sha256_hash, stored_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "name": db_user.name, "preferred_language": db_user.preferred_language, "age": db_user.age}