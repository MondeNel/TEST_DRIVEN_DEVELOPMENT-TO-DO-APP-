import pytest
from httpx import AsyncClient
from fastapi import status
from bson import ObjectId
from unittest.mock import AsyncMock, patch

from app.main import app  

@pytest.mark.asyncio
async def test_create_todo_route():
    """
    Test the POST /todos route to ensure a new todo can be created.
    """
    # Input data for the request
    todo_data = {"task": "Write unit tests"}

    # Simulated inserted ID and returned todo
    fake_id = ObjectId()
    expected_todo = {"id": str(fake_id), "task": "Write unit tests"}

    # Patch the `create_todo` function from the crud module
    with patch("app.routes.crud.create_todo", new_callable=AsyncMock) as mock_create:
        mock_create.return_value = expected_todo

        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/todos", json=todo_data)

        # Check that the mocked function was called correctly
        mock_create.assert_awaited_once_with(todo_data)

        # Validate the response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_todo
