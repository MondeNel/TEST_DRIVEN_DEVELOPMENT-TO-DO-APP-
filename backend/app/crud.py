from .database import todo_collection
from .models import todo_helper
from bson import ObjectId

# Create
async def create_todo(data: dict):
    todo = await todo_collection.insert_one(data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_helper(new_todo)

# Read all
async def get_all_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos

# Read one
async def get_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_helper(todo)

# Update
async def update_todo(id: str, data: dict):
    if len(data) < 1:
        return False
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        updated = await todo_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return updated.modified_count > 0
    return False

# Delete
async def delete_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        await todo_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
