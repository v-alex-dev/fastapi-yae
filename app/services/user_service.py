import asyncpg
from sqlalchemy.testing.pickleable import User

from app.db.database import get_pool
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.security import hash_password


async def create_user(user_data: UserCreate) -> User:
    """Insert a new user and return the created row (without password)."""

    pool = get_pool()
    hashed_password = hash_password(user_data.password)

    query = """
        INSERT INTO users (username, email, hashed_password)
        VALUES ($1, $2, $3)
        RETURNING id, username, is_active, created_at;
    """

    return await pool.fetchrow(query, user_data.username, user_data.email, hashed_password)

async def get_user_by_id(user_id: int) -> User:
    """Fetch a single user by id, or None if it does not exist."""

    pool = get_pool()
    query = """
        SELECT id, username, is_active, created_at 
        FROM users 
        WHERE id = $1;
    """

    return await pool.fetchrow(query, user_id)


