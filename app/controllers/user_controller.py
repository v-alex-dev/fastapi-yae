import asyncpg

from fastapi import HTTPException
from app.services import user_service
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut

async def create_user(user_data: UserCreate) -> UserOut:
    """Create a new user. Returns 409 if username/email already exists."""
    try:
        record= await user_service.create_user(user_data)
    except asyncpg.UniqueViolationError:
        # Raised by PostgreSQL when a UNIQUE constraint (username/email) is violated.
        raise HTTPException(status_code=409, detail="Ussername or email already exists!")

    return UserOut.model_validate(record)

