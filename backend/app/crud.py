from bson import ObjectId
from app.database import todo_collection
from app.utils import todo_helper

# Create a new Todo document in the database
async def add_todo(todo_data: dict) -> dict:
    """
    Add a new todo to the database.

    Args:
        todo_data (dict): The todo data to insert.

    Returns:
        dict: The newly created todo formatted with helper.
    """
    todo = await todo_collection.insert_one(todo_data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_helper(new_todo)

# Retrieve all todos from the database
async def get_all_todos():
    """
    Fetch all todos from the database.

    Returns:
        list: A list of formatted todo documents.
    """
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos

# Retrieve a specific todo by its ID
async def get_todo_by_id(id: str):
    """
    Get a todo by its ID.

    Args:
        id (str): The todo's ObjectId string.

    Returns:
        dict or None: The formatted todo document or None if not found.
    """
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    return todo_helper(todo) if todo else None

# Update a todo by its ID
async def update_todo(id: str, data: dict):
    """
    Update a todo's fields by ID.

    Args:
        id (str): The ObjectId of the todo to update.
        data (dict): The fields to update.

    Returns:
        bool: True if update was successful, False otherwise.
    """
    update = await todo_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return update.modified_count > 0

# Delete a todo by its ID
async def delete_todo(id: str):
    """
    Delete a todo from the database by its ID.

    Args:
        id (str): The ObjectId of the todo to delete.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    result = await todo_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
