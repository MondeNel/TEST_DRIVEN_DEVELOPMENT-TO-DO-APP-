from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoInDB(TodoBase):
    id: str

    class Config:
        orm_mode = True
