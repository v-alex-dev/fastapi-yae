# app/controllers/health_controller.py
#
# Controllers handle the HTTP layer: they receive the request,
# call the appropriate service, and shape the response.
# They contain NO SQL and NO business logic themselves.

from fastapi import HTTPException
from app.services import health_service


async def get_health_status() -> dict:
    """Return the API status and the database connectivity status."""
    try:
        db_ok = await health_service.check_database_connection()
    except Exception:
        # If the DB check fails, return a 503 (Service Unavailable)
        raise HTTPException(status_code=503, detail="Database unavailable")

    return {
        "status": "ok",
        "database": "connected" if db_ok else "unreachable",
    }
