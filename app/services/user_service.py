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
        RETURNING id, username,email, is_active, created_at;
    """

    return await pool.fetchrow(query, user_data.username, user_data.email, hashed_password)

async def get_user_by_id(user_id: int) -> User:
    """Fetch a single user by id, or None if it does not exist."""

    pool = get_pool()
    query = """
        SELECT id, username,email, is_active, created_at 
        FROM users 
        WHERE id = $1;
    """

    return await pool.fetchrow(query, user_id)

async def get_user_by_email(email: str) -> User:
    pool = get_pool()
    query = """
        SELECT id, username,email, is_active, created_at
        FROM users
        WHERE email = $1;
    """
    return await pool.fetchrow(query, email)

async def list_users() -> list[asyncpg.Record]:
    """Fetch all users stored in the database, ordred by id."""
    pool = get_pool()
    query = """
        SELECT id, username,email, is_active, created_at
        FROM users
        ORDER BY id DESC;
    """
    return await pool.fetch(query)

async def update_user(user_id: int, user_data: UserUpdate) -> asyncpg.Record | None:
    """Partially update a user. Only fields provided in user_data are changed."""
    pool = get_pool()
    # Build the SET clause dynamically, based on which fields were sent.
    # We only ever interpolate FIELD NAMES that we wrote ourselves below
    # (never raw user input), and all VALUES go through $1, $2... placeholders.

    fields: list[str]= []
    values: list = []
    param_index = 1

    if user_data.username is not None:
        fields.append(f"username = ${param_index}")
        values.append(user_data.username)
        param_index += 1
    if user_data.email is not None:
        fields.append(f"email = ${param_index}")
        values.append(user_data.email)
        param_index += 1
    if user_data.password is not None:
        hashed_password = hash_password(user_data.password)
        fields.append(f"hashed_password = ${param_index}")
        values.append(hashed_password)
        param_index += 1

    if not fields:
        return await get_user_by_id(user_id)

    values.append(user_id)
    query = f"""
           UPDATE users
           SET {", ".join(fields)}
           WHERE id = ${param_index}
           RETURNING id, username, email, is_active, created_at;
       """
    return await pool.fetchrow(query, *values)

async def delete_user(user_id: int) -> int | None:
    """Delete a user by id. Returns the deleted id, or None if not found."""
    pool = get_pool()
    query = """DELETE FROM users WHERE id = $1 RETURNING id;"""
    return await pool.fetchrow(query, user_id)