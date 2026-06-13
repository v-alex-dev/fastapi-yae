# app/routes/health_routes.py
#
# Routes only declare the URL paths and HTTP methods.
# They delegate all the work to the controller.

from fastapi import APIRouter
from app.controllers import health_controller

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health_check():
    """Check that the API and the database are up and running."""
    return await health_controller.get_health_status()
