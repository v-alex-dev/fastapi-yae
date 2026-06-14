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
        raise HTTPException(status_code=409, detail="Username or email already exists!")

    return UserOut.model_validate(dict(record))

async def get_user(user_id: int)-> UserOut:
    """Fetch a single user by id. Returns 404 if not found."""
    record = await user_service.get_user_by_id(user_id)

    if record is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserOut.model_validate(dict(record))


async def list_users()-> list[UserOut]:
    """Fetch all users """
    records = await user_service.list_users()
    return [UserOut.model_validate(dict(record)) for record in records]

async def update_user(user_id:int ,user_data: UserUpdate) -> UserOut:
    """Update an existing user. Returns 404 if not found."""
    try:
        record = await user_service.update_user(user_id, user_data)
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=409, detail="Username or email already exists!")

    if record is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserOut.model_validate(dict(record))

async def delete_user(user_id:int)-> dict:
    """Delete an existing user. Returns 404 if not found."""
    deleted_id = await user_service.delete_user(user_id)
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": f"User {deleted_id} has been deleted"}