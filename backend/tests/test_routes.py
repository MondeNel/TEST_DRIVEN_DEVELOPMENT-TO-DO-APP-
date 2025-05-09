import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from bson import ObjectId
from unittest.mock import AsyncMock, patch
from app.main import app  

@pytest.mark.asyncio
async def test_update_todo_route():
    """
    Test the PUT /todos/{todo_id} route to ensure a todo is updated successfully.
    """
    fake_id = str(ObjectId())
    update_data = {"task": "Updated task"}
    expected_response = {"msg": "Todo updated"}

    with patch("app.routes.update_todo", new_callable=AsyncMock) as mock_update:
        mock_update.return_value = True

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://testserver") as client:
            response = await client.put(f"/todos/{fake_id}", json=update_data)

        mock_update.assert_awaited_once_with(fake_id, update_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_response

