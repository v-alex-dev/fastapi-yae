from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.controllers import auth_controller
from app.schemas.auth_schema import Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
        Authenticate a user and return a JWT token
        OAuth2PasswordRequestForm expect form_data with "username" and "password" fields.
    """

    return await auth_controller.login(form_data.username, form_data.password)