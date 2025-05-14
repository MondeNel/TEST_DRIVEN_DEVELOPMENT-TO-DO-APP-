from .database import todo_collection
from .models import todo_helper
from bson import ObjectId
from bson.errors import InvalidId

# Create
async def create_todo(data: dict):
    """
    Create a new todo item.

    Args:
        data (dict): The todo data to insert.

    Returns:
        dict: The inserted todo item.
    """
    todo = await todo_collection.insert_one(data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_helper(new_todo)


# Read all
async def get_all_todos():
    """
    Retrieve all todo items.

    Returns:
        list: List of all todos.
    """
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos


# Read one
async def get_todo(id: str):
    """
    Retrieve a single todo item by its ID.

    Args:
        id (str): The ID of the todo item.

    Returns:
        dict or None: The found todo item or None.
    """
    try:
        todo = await todo_collection.find_one({"_id": ObjectId(id)})
        if todo:
            return todo_helper(todo)
    except InvalidId:
        return None


async def update_todo(id: str, data: dict) -> bool:
    """
    Update a todo item by its ID.

    Args:
        id (str): The ID of the todo item.
        data (dict): The fields to update.

    Returns:
        bool: True if updated, False otherwise.
    """
    try:
        if len(data) < 1:
            return False

        result = await todo_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )

        return result.modified_count > 0 or result.matched_count > 0

    except InvalidId:
        return False
    except Exception as e:
        print(f"Update error: {e}")
        return False



# Delete function
async def delete_todo(id: str):
    """
    Delete a todo item by its ID.

    Args:
        id (str): The ID of the todo item.

    Returns:
        bool: True if deleted, False otherwise.
    """
    try:
        todo = await todo_collection.find_one({"_id": ObjectId(id)})
        if todo:
            await todo_collection.delete_one({"_id": ObjectId(id)})
            return True
    except InvalidId:
        return False
    return False
