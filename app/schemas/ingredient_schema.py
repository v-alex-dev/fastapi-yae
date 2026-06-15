from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

class IngredientCreate(BaseModel):
    name: str

class IngredientUpdate(BaseModel):
    id: int
    name: str

class IngredientDelete(BaseModel):
    id: int

class IngredientOut(BaseModel):
    id: int
    name: str
    creation_date: datetime