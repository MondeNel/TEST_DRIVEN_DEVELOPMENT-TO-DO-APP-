import pytest
from app.crud import add_todo
from app.database import todo_collection
from bson import ObjectId


@pytest.mark.asyncio
async def test_add_todo():
    """
    Test the add_todo function to ensure a todo is added correctly.
    """
    # Example data to add a todo
    todo_data = {"title": "Test Todo", "description": "Test description"}
    
    # Call the add_todo function
    result = await add_todo(todo_data)

    # Assertions
    assert result["title"] == todo_data["title"]
    assert result["description"] == todo_data["description"]
    assert isinstance(result["id"], str)

    # Clean up: Remove the added todo from the database
    await todo_collection.delete_one({"_id": ObjectId(result["id"])})
