from fastapi import APIRouter, HTTPException
from .schemas import TodoCreate, TodoInDB
from . import crud
from .models import todo_helper
from .database import todo_collection
from bson import ObjectId


router = APIRouter()

@router.post("/todos", response_model=TodoInDB)
async def create_todo(todo: TodoCreate):
    return await crud.create_todo(todo.dict())

@router.get("/todos", response_model=list[TodoInDB])
async def read_todos():
    return await crud.get_all_todos()

@router.get("/todos/{todo_id}", response_model=TodoInDB)
async def read_todo(todo_id: str):
    todo = await crud.get_todo(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/todos/{todo_id}", response_model=TodoInDB)
async def update_todo(todo_id: str, todo: TodoCreate):
    success = await crud.update_todo(todo_id, todo.dict())
    if success:
        updated = await todo_collection.find_one({"_id": ObjectId(todo_id)})
        if updated:
            return todo_helper(updated)
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    success = await crud.delete_todo(todo_id)
    if success:
        return {"msg": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
