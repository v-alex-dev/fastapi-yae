from fastapi import HTTPException, status

from app.services.auth_service import authenticate_user
from app.utils.security import create_access_token
from app.schemas.auth_schema import Token

async def login(username:str, password:str)-> Token:
    """Validate credentials and return a JWT access token."""
    user = await authenticate_user(username, password)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(username = user["username"])
    return Token(access_token = access_token)
