import asyncpg

from fastapi import HTTPException
from app.services import ingredient_service
from app.schemas.ingredient_schema import IngredientUpdate, IngredientCreate, IngredientDelete, IngredientOut


async def create_ingredient(ingredient: IngredientCreate) -> IngredientOut:

    if ingredient is None:
        raise HTTPException(status_code=400, detail="Ingredient is required")

    return await ingredient_service.ingredient_create(ingredient)

async def list_ingredients() -> list[asyncpg.Record]:
    return await ingredient_service.list_ingredients()

async def update_ingredient(ingredient: IngredientUpdate) -> IngredientOut:
    if ingredient is None:
        raise HTTPException(status_code=400, detail="Ingredient is required")

    return await ingredient_service.ingredient_update(ingredient)

async def delete_ingredient(ingredient_id: int)-> asyncpg.Record:
    return await ingredient_service.ingredient_delete(ingredient_id)