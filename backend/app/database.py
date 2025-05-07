from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# Initialize the MongoDB client and database
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db
todo_collection: Collection = db.get_collection("todos")


async def create_db_and_collections():
    """
    Ensure the 'todos' collection exists in the database.
    """
    if "todos" not in await db.list_collection_names():
        await db.create_collection("todos")
