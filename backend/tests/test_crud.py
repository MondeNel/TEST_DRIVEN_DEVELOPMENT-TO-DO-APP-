import pytest
from app import crud
from app.database import todo_collection
from bson import ObjectId

@pytest.mark.asyncio
async def test_create_todo():
    todo_data = {"title": "Test Add", "description": "Add description", "completed": False}
    result = await crud.create_todo(todo_data)

    assert result["title"] == todo_data["title"]
    assert result["description"] == todo_data["description"]

    # Cleanup
    await todo_collection.delete_one({"_id": ObjectId(result["id"])})

@pytest.mark.asyncio
async def test_get_all_todos():
    todo_data = {"title": "Test List", "description": "List description", "completed": False}
    created = await crud.create_todo(todo_data)

    todos = await crud.get_all_todos()
    assert isinstance(todos, list)
    assert any(todo["title"] == "Test List" for todo in todos)

    # Cleanup
    await todo_collection.delete_one({"_id": ObjectId(created["id"])})

@pytest.mark.asyncio
async def test_get_todo():
    todo_data = {"title": "Test By ID", "description": "Get ID", "completed": False}
    created = await crud.create_todo(todo_data)

    fetched = await crud.get_todo(created["id"])
    assert fetched["title"] == todo_data["title"]

    # Cleanup
    await todo_collection.delete_one({"_id": ObjectId(created["id"])})

@pytest.mark.asyncio
async def test_update_todo():
    todo_data = {"title": "Before Update", "description": "Old", "completed": False}
    created = await crud.create_todo(todo_data)

    update_data = {"title": "After Update"}
    success = await crud.update_todo(created["id"], update_data)
    assert success is True

    updated = await crud.get_todo(created["id"])
    assert updated["title"] == "After Update"

    # Cleanup
    await todo_collection.delete_one({"_id": ObjectId(created["id"])})

@pytest.mark.asyncio
async def test_delete_todo():
    todo_data = {"title": "To Be Deleted", "description": "Delete me", "completed": False}
    created = await crud.create_todo(todo_data)

    success = await crud.delete_todo(created["id"])
    assert success is True

    deleted = await crud.get_todo(created["id"])
    assert deleted is None
