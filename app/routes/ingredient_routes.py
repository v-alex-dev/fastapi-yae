from fastapi import APIRouter, status, Depends
from sqlalchemy.testing.pickleable import User

from app.controllers import ingredient_controller
from app.schemas.ingredient_schema import IngredientCreate, IngredientUpdate, IngredientOut
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.post("/new", response_model=IngredientOut, status_code=status.HTTP_201_CREATED)
async def ingredient_create(ingredient: IngredientCreate, current_user = Depends(get_current_user)):
    """Create a new personal ingredient for the current user."""
    return await ingredient_controller.create_ingredient(ingredient, current_user)

@router.get("/all", response_model=list[IngredientOut])
async def ingredient_list(current_user = Depends(get_current_user)):
    """List all ingredients (global and personal)."""
    return await ingredient_controller.list_ingredients(current_user)

@router.patch("/",response_model=IngredientOut)
async def ingredient_update(ingredient: IngredientUpdate, current_user = Depends(get_current_user)) -> IngredientOut:
    return await ingredient_controller.update_ingredient(ingredient, current_user)


@router.delete("/{ingredient_id}")
async def ingredient_delete(ingredient_id: int, current_user = Depends(get_current_user)):
    """Delete an ingredient. Only the owner can delete it."""
    return await ingredient_controller.delete_ingredient(ingredient_id, current_user)