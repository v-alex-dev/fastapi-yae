from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    """data required to create a new user (input)"""

    username: str
    email: EmailStr
    password: str

