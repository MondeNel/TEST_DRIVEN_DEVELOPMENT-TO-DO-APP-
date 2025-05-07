from pydantic import BaseModel, Field
from typing import Optional

# This schema defines the structure and validation rules for creating a new Todo item.
class TodoSchema(BaseModel):
    title: str = Field(..., example="Read a book")  # Required field with an example
    description: Optional[str] = Field(None, example="Finish reading Dune")  # Optional field with example

# This schema defines the structure for updating a Todo item.
# All fields are optional since PATCH or PUT may update just one or more fields.
class UpdateTodoSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]

# This schema represents the shape of the response returned to the client.
# It extends the base Todo schema and adds an ID field for the document.
class TodoResponse(TodoSchema):
    id: str  # ID returned from MongoDB, represented as a string
