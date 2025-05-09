from pydantic import BaseModel, ConfigDict
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoInDB(TodoBase):
    id: str

    model_config = ConfigDict(from_attributes=True)
