import asyncpg

from app.db.database import get_pool
from app.schemas.ingredient_schema import IngredientCreate, IngredientUpdate, IngredientOut

async def ingredient_create(name: str, user_id: int) -> IngredientOut:
    """
        Insert a new ingredient.
        user_id is None for global ingredients, or the id of the user
        who created a personal ingredient.
    """

    pool =  get_pool()

    query = """
        INSERT INTO ingredients (name,user_id)
        VALUES($1, $2)
        RETURNING id, name, created_at;
    """

    return await pool.fetchrow(query, name, user_id)

async def ingredient_update(ingredient_id: int, name: str) -> asyncpg.Record | None:
    """Update the name of an existing ingredient.

    Returns None if no ingredient was found with this id.
    """
    pool = get_pool()

    query = """
        UPDATE Ingredients
        SET name = $1,
        WHERE id = $2,
        RETURNING id, name,user_id, created_at;
    """

    return await pool.fetchrow(query, name, ingredient_id)

async def get_ingredient_by_id(ingredient_id: int) -> asyncpg.Record | None:
    pool = get_pool()
    query = """
    SELECT id, name FROM Ingredient WHERE id = $1;
    """
    return await pool.fetchrow(query, ingredient_id)

async def list_ingredients() -> list[asyncpg.Record]:
    pool = get_pool()
    query =""""
        SELECT id, name
        FROM Ingredient
        ORDER BY name DESC;
    """
    return await pool.fetch(query)

async def ingredient_delete(ingredient_id: int) -> asyncpg.Record | None:
    pool = get_pool()
    query = """
    DELETE FROM Ingredient WHERE id = $1 RETURNING id;
    """
    return await pool.fetchrow(query, ingredient_id)
