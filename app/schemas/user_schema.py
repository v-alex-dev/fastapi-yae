from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    """data required to create a new user (input)"""

    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    """Data allowed when updating a user (input).

    All fields are optional: the client can send only the fields
    they want to change.
    """

    username: str | None
    email: EmailStr | None
    password: str | None

class UserOut(BaseModel):
    """Data returned to the client (output).

    Notice there is NO password field here: we never expose it,
    not even the hashed version.
    """

    id:int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    # Allows creating this schema directly from an asyncpg Record
    # (or any object with attributes), not just from a dict.
    model_config = ConfigDict(from_attributes=True)