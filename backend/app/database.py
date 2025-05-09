from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Ensure the URI is properly retrieved
MONGODB_URI = os.getenv("MONGODB_URI")

# Decode any improperly encoded characters
if MONGODB_URI:
    MONGODB_URI = MONGODB_URI.encode("utf-8").decode("unicode_escape")

print("Loaded MONGODB_URI:", MONGODB_URI)  # Debugging

if not MONGODB_URI.startswith("mongodb://") and not MONGODB_URI.startswith("mongodb+srv://"):
    raise ValueError("MONGODB_URI is incorrectly formatted!")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)

# Define the database and collection
database = client.todo_db
todo_collection = database.get_collection("todos")
