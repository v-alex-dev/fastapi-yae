from pydantic import BaseModel

class Token(BaseModel):
    """Response returned by the auth/login endpoint"""
    access_token: str
    token_type: str = "bearer"

