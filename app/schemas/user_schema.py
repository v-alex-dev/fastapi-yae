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

