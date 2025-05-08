import pytest
import httpx
from app.main import app
from app.database import todo_collection

@pytest.fixture(scope="module")
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope="function")
async def client():
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac


@pytest.mark.anyio
async def test_create_todo(client):
    payload = {"title": "Test route todo", "description": "Testing create route"}
    response = await client.post("/todos", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]

    # Cleanup
    await todo_collection.delete_one({"_id": data["id"]})


@pytest.mark.anyio
async def test_read_all_todos(client):
    response = await client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.anyio
async def test_get_todo_by_id(client):
    todo = {"title": "Fetch by ID", "description": "Get this one"}
    inserted = await todo_collection.insert_one(todo)
    inserted_id = str(inserted.inserted_id)

    response = await client.get(f"/todos/{inserted_id}")
    assert response.status_code == 200
    assert response.json()["title"] == todo["title"]

    await todo_collection.delete_one({"_id": inserted.inserted_id})


@pytest.mark.anyio
async def test_update_todo(client):
    todo = {"title": "Old title", "description": "Old desc"}
    inserted = await todo_collection.insert_one(todo)
    inserted_id = str(inserted.inserted_id)

    update_data = {"title": "New title"}
    response = await client.patch(f"/todos/{inserted_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Todo updated successfully"

    await todo_collection.delete_one({"_id": inserted.inserted_id})


@pytest.mark.anyio
async def test_delete_todo(client):
    todo = {"title": "To delete", "description": "Remove me"}
    inserted = await todo_collection.insert_one(todo)
    inserted_id = str(inserted.inserted_id)

    response = await client.delete(f"/todos/{inserted_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted successfully"
