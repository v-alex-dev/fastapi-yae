from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.config.settings import settings
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Turn a plain-text password into a secure hash for storage."""
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plain-text password against a stored hash.

    Used during login: we never decrypt the stored hash,
    we just hash the input again and compare the results.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(username: str) -> str:
    """Create a signed JWT containing the username and an expiration date.

    The "sub" (subject) claim is the standard JWT field used to
    identify the user the token belongs to.
    """
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {"sub": username, "exp": expire}

    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

def decode_access_token(token: str) -> str | None:
    """Decode a JWT and return the username (the "sub" claim).

    Returns None if the token is invalid or expired,
    so the caller can turn that into a 401 error.
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload.get("sub")
    except JWTError:
        return None