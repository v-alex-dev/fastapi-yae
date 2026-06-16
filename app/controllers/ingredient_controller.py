import asyncpg

from fastapi import HTTPException
from sqlalchemy.sql.functions import current_user

from app.services import ingredient_service
from app.schemas.ingredient_schema import IngredientUpdate, IngredientCreate, IngredientOut


async def create_ingredient(ingredient: IngredientCreate, current_user) -> IngredientOut:
    """Create a new personal ingredient for the current user.

    Returns 409 if an ingredient with the same name already exists.
    """
    try:
        record = await ingredient_service.ingredient_create(
            name=ingredient.name,
            user_id=current_user["id"]
        )
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Ingredient already exists")

    return record

async def list_ingredients() -> list[IngredientOut]:
    """List all ingredients (global ones and every user's personal ones)."""
    records = await ingredient_service.list_ingredients()

    return [IngredientOut.model_validate(dict(record) for record in records)]

async def update_ingredient(ingredient: IngredientUpdate, current_user) -> IngredientOut:
    """Update an ingredient's name.

    Only the user who owns the ingredient can update it.
    Global ingredients (user_id is None) cannot be updated by anyone yet.
    """

    existing = await ingredient_service.get_ingredient_by_id(ingredient.id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    if existing["user_id"] != current_user["id"]:
        raise HTTPException(status_code=400, detail="You cannot modify this ingredient")

    try:
        record = await ingredient_service.ingredient_update(ingredient.id, ingredient.name)
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Ingredient already exists")
    return IngredientOut.model_validate(dict(record))


async def delete_ingredient(ingredient_id: int, current_user)-> dict:
    """Delete an ingredient.

    Only the user who owns the ingredient can delete it.
    """
    existing = await ingredient_service.get_ingredient_by_id(ingredient_id)

    if existing is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    if existing["user_id"] != current_user["id"]:
        raise HTTPException(status_code=400, detail="You cannot delete this ingredient")

    await ingredient_service.ingredient_delete(ingredient_id)
    return {"details": f"{ingredient_id} has been deleted"}