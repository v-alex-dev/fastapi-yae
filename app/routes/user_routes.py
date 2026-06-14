# app/routes/user_routes.py
#
# Routes only declare URL paths and HTTP methods.
# They delegate everything to the controller.


from fastapi import APIRouter, status
from app.controllers import user_controller
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate) -> UserOut:
    """create a new user"""
    return await user_controller.create_user(user_data)

@router.get("/", response_model=list[UserOut])
async def list_users():
    """list all users"""
    return await user_controller.list_users()