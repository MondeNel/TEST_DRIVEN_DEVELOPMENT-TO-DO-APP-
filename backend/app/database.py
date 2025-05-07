# Handles MongoDB client initialization and connection
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db
todo_collection: Collection = db.get_collection("todos")

async def create_db_and_collections():
    await db.create_collection("todos") if "todos" not in await db.list_collection_names() else None
