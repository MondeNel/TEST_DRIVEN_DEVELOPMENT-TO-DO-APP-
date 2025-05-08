# MongoDB doesn't require models like relational DBs, but you can use utility functions
from bson import ObjectId

def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description", ""),
        "completed": todo["completed"]
    }
