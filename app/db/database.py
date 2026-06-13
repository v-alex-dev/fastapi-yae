# app/db/database.py
#
# This module manages the asyncpg connection pool.
# A "pool" reuses a fixed number of open connections instead of opening
# a new connection for every request, which is much more efficient.

import asyncpg
from app.config.settings import settings

# Module-level variable holding the pool once it is created.
# It starts as None and is set during application startup (see main.py).
pool: asyncpg.Pool | None = None


async def connect_to_db() -> None:
    """Create the connection pool. Called once when the app starts."""
    global pool
    pool = await asyncpg.create_pool(
        dsn=settings.database_dsn,
        min_size=1,
        max_size=10,
    )


async def disconnect_from_db() -> None:
    """Close the connection pool. Called once when the app stops."""
    global pool
    if pool is not None:
        await pool.close()


def get_pool() -> asyncpg.Pool:
    """Return the active pool, raising an error if it was not initialized."""
    if pool is None:
        raise RuntimeError("Database pool is not initialized yet.")
    return pool
