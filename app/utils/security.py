from passlib.context import CryptContext

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