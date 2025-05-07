# Main entry point for the FastAPI application
from fastapi import FastAPI
from app.routes import router
from app.database import create_db_and_collections

# Create the FastAPI application instance with a title
app = FastAPI(title="Todo API")

# Include the route handlers from app/routes.py
app.include_router(router)

# Hook to run on application startup
@app.on_event("startup")
async def startup_event():
    """
    Function that runs once when the application starts.
    It ensures the necessary MongoDB database and collections are created.
    """
    await create_db_and_collections()
