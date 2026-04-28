from fastapi import FastAPI

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

# Include authentication routes
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(analysis)