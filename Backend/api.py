from fastapi import FastAPI

# Import for CORS (Cross-Origin Resource Sharing) to allow frontend to talk to backend
from fastapi.middleware.cors import CORSMiddleware  
from fastapi.staticfiles import StaticFiles 
import os 

# Import local files
import database
import models
from routers.authentication import router as auth_router
from routers.users import router as users_router
from routers.posts import router as posts_router
from routers.analysis import router as analysis

# Create the database tables automatically (if they don't exist yet)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Skin Secure API")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://skinsecure.streamlit.app"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], # Allowed HTTP methods like GET, POST, PUT, DELETE
    allow_headers=["Content-Type", "Authorization", "Accept"],  # Allowed headers like Content-Type, Authorization
)

# Set up static file serving for uploaded images
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Include authentication routes
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(analysis)