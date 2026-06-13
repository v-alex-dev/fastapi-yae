# app/services/health_service.py
#
# Services contain the "business logic" and the actual SQL queries.
# Controllers call services; services never talk to the HTTP layer directly.

from app.db.database import get_pool


async def check_database_connection() -> bool:
    """Run a trivial SQL query to confirm the database is reachable."""
    pool = get_pool()

    # "SELECT 1" is a classic way to check that a connection works
    # without depending on any table existing yet.
    result = await pool.fetchval("SELECT 1;")

    return result == 1
