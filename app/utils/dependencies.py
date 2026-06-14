from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.services.user_service import get_user_by_username
from app.utils.security import decode_access_token

# Tells FastAPI/Swagger where to send the username/password
# to get a token (used for the "Authorize" button).
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
        Decode the JWT from the Authorization header and return the user.
        Raises 401 if the token is invalid, expired, or the user
        no longer exists in the database.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username = decode_access_token(token)
    if username is None:
        raise credentials_exception

    user = await get_user_by_username(username=username)
    if user is None:
        raise credentials_exception
    return user