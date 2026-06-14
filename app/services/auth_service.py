from app.services.user_service import  get_user_by_username
from app.utils.security import verify_password

async def authenticate_user(username: str, password: str):
    """Check username/password and return the user record if valid.

    Returns None if the username does not exist or the password
    is incorrect. The caller turns this into a 401 error.
    """
    user = await get_user_by_username(username)

    if user is None:
        return None

    if not verify_password(password, user['hashed_password']):
        return None

    return user