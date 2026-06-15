# app/routes/user_routes.py
#
# Routes only declare URL paths and HTTP methods.
# They delegate everything to the controller.


from fastapi import APIRouter, status, Depends
from app.controllers import user_controller
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
async def get_me(current_user = Depends(get_current_user)):
    return await user_controller.get_current_user_info(current_user)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate) -> UserOut:
    """create a new user"""
    return await user_controller.create_user(user_data)

@router.get("/", response_model=list[UserOut])
async def list_users():
    """list all users"""
    return await user_controller.list_users()



#@router.get("/{user_id}", response_model=UserOut)
#async def read_user(user_id: int)) -> UserOut:
    """get a single user by id"""
    return await user_controller.get_user(user_id)

@router.patch("/{user_id}", response_model=UserOut)
async def update_user(user_id:int, user_data: UserUpdate, current_user = Depends(get_current_user)) -> UserOut:
    """Partially update a user"""
    return await user_controller.update_user(user_id, user_data, current_user)

@router.delete("/{user_id}")
async def delete_user(user_id: int, current_user = Depends(get_current_user)):
    """delete a user"""
    return await user_controller.delete_user(user_id, current_user)

