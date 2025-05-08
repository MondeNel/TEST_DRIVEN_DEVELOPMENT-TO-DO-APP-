import pytest
from unittest.mock import AsyncMock, patch
from bson import ObjectId
from app.crud import create_todo, get_all_todos, get_todo

class AsyncIteratorMock:
    """Helper class to mock async iterators"""
    def __init__(self, items):
        self.items = iter(items)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.items)
        except StopIteration:
            raise StopAsyncIteration


@pytest.mark.asyncio
async def test_create_todo():
    test_data = {"task": "Write tests"}
    fake_id = ObjectId()
    inserted_todo = {"_id": fake_id, "task": "Write tests"}
    expected_result = {"id": str(fake_id), "task": "Write tests"}  # assuming todo_helper formats like this

    with patch("app.crud.todo_collection.insert_one", new_callable=AsyncMock) as mock_insert, \
         patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find, \
         patch("app.crud.todo_helper", return_value=expected_result) as mock_helper:

        mock_insert.return_value.inserted_id = fake_id
        mock_find.return_value = inserted_todo

        result = await create_todo(test_data)

        mock_insert.assert_awaited_once_with(test_data)
        mock_find.assert_awaited_once_with({"_id": fake_id})
        mock_helper.assert_called_once_with(inserted_todo)

        assert result == expected_result

@pytest.mark.asyncio
async def test_get_all_todos():
    # Mock data to simulate the response from the database
    mock_todos = [
        {"_id": 1, "task": "Test Task 1"},
        {"_id": 2, "task": "Test Task 2"}
    ]
    expected_result = [
        {"id": "1", "task": "Test Task 1"},
        {"id": "2", "task": "Test Task 2"}
    ]

    # Patch the todo_collection.find() method to return an async iterator
    with patch("app.crud.todo_collection.find", new_callable=AsyncMock) as mock_find, \
         patch("app.crud.todo_helper") as mock_helper:

        # Set the mock to return the mock todos
        mock_find.return_value = AsyncIteratorMock(mock_todos)
        
        # Mock the helper to return the expected result
        mock_helper.side_effect = lambda todo: {"id": str(todo["_id"]), "task": todo["task"]}

        # Call the function being tested
        result = await get_all_todos()

        # Assertions to check that the mocks were called and the result is correct
        mock_find.assert_awaited_once()
        mock_helper.assert_any_call(mock_todos[0])
        mock_helper.assert_any_call(mock_todos[1])

        # Assert that the result is correct
        assert result == expected_result


@pytest.mark.asyncio
async def test_get_todo_found():
    mock_id = ObjectId()
    mock_todo = {"_id": mock_id, "task": "Test Task"}
    expected_result = {"id": str(mock_id), "task": "Test Task"}

    # Patch the todo_collection.find_one() method
    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find, \
         patch("app.crud.todo_helper") as mock_helper:

        # Set the mock to return the mock todo
        mock_find.return_value = mock_todo
        
        # Mock the helper to return the expected result
        mock_helper.side_effect = lambda todo: {"id": str(todo["_id"]), "task": todo["task"]}

        # Call the function being tested
        result = await get_todo(str(mock_id))

        # Assertions to check that the mocks were called and the result is correct
        mock_find.assert_awaited_once_with({"_id": mock_id})
        mock_helper.assert_called_once_with(mock_todo)

        # Assert that the result is correct
        assert result == expected_result


@pytest.mark.asyncio
async def test_get_todo_not_found():
    # Create a fake ObjectId
    mock_id = ObjectId()

    # Patch find_one to return None (simulating no document found)
    with patch("app.crud.todo_collection.find_one", new_callable=AsyncMock) as mock_find:
        mock_find.return_value = None

        result = await get_todo(str(mock_id))

        # Check that find_one was called with the correct filter
        mock_find.assert_awaited_once_with({"_id": mock_id})
        
        # The function should return None if no document is found
        assert result is None