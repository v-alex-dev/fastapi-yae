import asyncpg

from app.db.database import get_pool
from app.schemas.ingredient_schema import IngredientCreate, IngredientUpdate, IngredientDelete, IngredientOut

async def ingredient_create(ingredient: IngredientCreate) -> IngredientOut:
    """create ingredient """

    pool =  get_pool()

    query = """
        INSERT INTO Ingredient (ingredient_name)
        VALUES($1)
        RETURNING id, name, created_at;
    """

    return await pool.fetchrow(query, ingredient.name)


