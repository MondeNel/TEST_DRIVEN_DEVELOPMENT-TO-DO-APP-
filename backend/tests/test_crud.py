import pytest
from unittest.mock import AsyncMock, patch
from bson import ObjectId
from app.crud import create_todo

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
