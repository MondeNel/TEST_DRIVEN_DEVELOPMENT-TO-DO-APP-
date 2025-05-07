# Defines API routes and integrates CRUD functions with FastAPI endpoints

from fastapi import APIRouter, HTTPException
from app.schemas import TodoSchema, UpdateTodoSchema
from app.crud import add_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo

# Create a new APIRouter instance for grouping routes
router = APIRouter()

@router.post("/todos")
async def create(todo: TodoSchema):
    """
    Create a new todo item.
    """
    return await add_todo(todo.dict())

@router.get("/todos")
async def read_all():
    """
    Retrieve all todo items.
    """
    return await get_all_todos()

@router.get("/todos/{id}")
async def read_one(id: str):
    """
    Retrieve a specific todo item by ID.
    """
    todo = await get_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.patch("/todos/{id}")
async def update(id: str, todo: UpdateTodoSchema):
    """
    Update a todo item partially by ID.
    Only fields provided will be updated.
    """
    updated = await update_todo(id, todo.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo updated successfully"}

@router.delete("/todos/{id}")
async def delete(id: str):
    """
    Delete a todo item by ID.
    """
    deleted = await delete_todo(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
