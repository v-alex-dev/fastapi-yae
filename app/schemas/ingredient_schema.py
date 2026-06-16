from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

class IngredientCreate(BaseModel):
    """Data required to create a new ingredient (input)."""
    name: str

class IngredientUpdate(BaseModel):
    """Data allowed when updating an ingredient (input)."""
    id: int
    name: str


class IngredientOut(BaseModel):
    """Data returned to the client (output)."""
    id: int
    name: str
    user_id: int | None
    created_at: datetime