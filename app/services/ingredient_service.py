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

async def ingredient_update(ingredient: IngredientUpdate) -> IngredientOut:
    """update ingredient """
    pool = get_pool()

    query = """
        UPDATE Ingredient
        SET name = $1,
        WHERE id = $2,
        RETURNING id, name, created_at;
    """

    return await pool.fetchrow(query, ingredient.name, ingredient.id)

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
