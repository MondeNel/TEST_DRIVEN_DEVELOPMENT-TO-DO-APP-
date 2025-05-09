def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),  # Convert ObjectId to string
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"]
    }