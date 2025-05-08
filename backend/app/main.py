from fastapi import FastAPI
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set the frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
