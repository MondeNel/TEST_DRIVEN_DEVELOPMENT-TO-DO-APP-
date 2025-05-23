import pytest
from unittest.mock import AsyncMock, patch
from bson import ObjectId
from app.crud import create_todo, get_all_todos, get_todo, update_todo, delete_todo

# Helper class to mock asynchronous iteration over database query results
class AsyncIteratorMock:
    """Helper class to mock async iterators (e.g. cursor returned by find())"""
    def __init__(self, items):
        self.items = iter(items)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.items)
        except StopIteration:
            raise StopAsyncIteration

# -------------------------
# Test: Create a new todo
# -------------------------
@pytest.mark.asyncio
async def test_create_todo():
    test_data = {"task": "Write tests"}
    fake_id = ObjectId()
    inserted_todo = {"_id": fake_id, "task": "Write tests"}
    expected_result = {"id": str(fake_id), "task": "Write tests"}

    # Mock database insert, find, and helper conversion
    with patch("app.crud.todo_collection.insert_one", new_callable=AsyncMock) as mock_insert, \
         patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find, \
         patch("app.crud.todo_helper", return_value=expected_result) as mock_helper:

        mock_insert.return_value.inserted_id = fake_id
        mock_find.return_value = inserted_todo

        # Call the function
        result = await create_todo(test_data)

        # Assert calls and result
        mock_insert.assert_awaited_once_with(test_data)
        mock_find.assert_awaited_once_with({"_id": fake_id})
        mock_helper.assert_called_once_with(inserted_todo)
        assert result == expected_result

# -----------------------------------
# Test: Get all todos from database
# -----------------------------------
@pytest.mark.asyncio
async def test_get_all_todos():
    mock_todos = [
        {"_id": 1, "task": "Test Task 1"},
        {"_id": 2, "task": "Test Task 2"},
    ]
    expected_result = [
        {"id": "1", "task": "Test Task 1"},
        {"id": "2", "task": "Test Task 2"},
    ]

    # Mock .find() to return an async iterator
    with patch("app.crud.todo_collection.find", return_value=AsyncIteratorMock(mock_todos)) as mock_find, \
         patch("app.crud.todo_helper") as mock_helper:

        mock_helper.side_effect = lambda todo: {"id": str(todo["_id"]), "task": todo["task"]}

        result = await get_all_todos()

        mock_find.assert_called_once()
        mock_helper.assert_any_call(mock_todos[0])
        mock_helper.assert_any_call(mock_todos[1])
        assert result == expected_result

# ---------------------------------------
# Test: Get one todo by ID (found case)
# ---------------------------------------
@pytest.mark.asyncio
async def test_get_todo_found():
    mock_id = ObjectId()
    mock_todo = {"_id": mock_id, "task": "Test Task"}
    expected_result = {"id": str(mock_id), "task": "Test Task"}

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find, \
         patch("app.crud.todo_helper") as mock_helper:

        mock_find.return_value = mock_todo
        mock_helper.return_value = expected_result

        result = await get_todo(str(mock_id))

        mock_find.assert_awaited_once_with({"_id": mock_id})
        mock_helper.assert_called_once_with(mock_todo)
        assert result == expected_result

# ------------------------------------------
# Test: Get one todo by ID (not found case)
# ------------------------------------------
@pytest.mark.asyncio
async def test_get_todo_not_found():
    mock_id = ObjectId()

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find:
        mock_find.return_value = None

        result = await get_todo(str(mock_id))

        mock_find.assert_awaited_once_with({"_id": mock_id})
        assert result is None

# ------------------------------------------
# Test: Update todo - should fail on empty data
# ------------------------------------------
@pytest.mark.asyncio
async def test_update_todo_empty_data():
    fake_id = str(ObjectId())
    result = await update_todo(fake_id, {})
    assert result is False

# ------------------------------------------
# Test: Successfully update a todo
# ------------------------------------------
@pytest.mark.asyncio
async def test_update_todo_success():
    fake_id = ObjectId()
    update_data = {"task": "Updated Task"}

    mock_update_result = AsyncMock()
    mock_update_result.modified_count = 1

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find_one, \
         patch("app.crud.todo_collection.update_one", new_callable=AsyncMock) as mock_update_one:

        mock_find_one.return_value = {"_id": fake_id, "task": "Old Task"}
        mock_update_one.return_value = mock_update_result

        result = await update_todo(str(fake_id), update_data)

        mock_find_one.assert_awaited_once_with({"_id": fake_id})
        mock_update_one.assert_awaited_once_with({"_id": fake_id}, {"$set": update_data})
        assert result is True

# ----------------------------------------------------
# Test: Update todo - should fail if todo not found
# ----------------------------------------------------
@pytest.mark.asyncio
async def test_update_todo_not_found():
    fake_id = ObjectId()
    update_data = {"task": "Updated Task"}

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find_one:
        mock_find_one.return_value = None

        result = await update_todo(str(fake_id), update_data)

        mock_find_one.assert_awaited_once_with({"_id": fake_id})
        assert result is False

# ----------------------------------------
# Test: Successfully delete an existing todo
# ----------------------------------------
@pytest.mark.asyncio
async def test_delete_todo_success():
    fake_id = ObjectId()

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find_one, \
         patch("app.crud.todo_collection.delete_one", new_callable=AsyncMock) as mock_delete_one:

        mock_find_one.return_value = {"_id": fake_id, "task": "Delete Me"}
        mock_delete_one.return_value = AsyncMock()

        result = await delete_todo(str(fake_id))

        mock_find_one.assert_awaited_once_with({"_id": fake_id})
        mock_delete_one.assert_awaited_once_with({"_id": fake_id})
        assert result is True

# ---------------------------------------
# Test: Fail to delete a todo (not found)
# ---------------------------------------
@pytest.mark.asyncio
async def test_delete_todo_not_found():
    fake_id = ObjectId()

    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find_one:
        mock_find_one.return_value = None

        result = await delete_todo(str(fake_id))

        mock_find_one.assert_awaited_once_with({"_id": fake_id})
        assert result is False
