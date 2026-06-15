from fastapi import APIRouter, status, Depends
from sqlalchemy.testing.pickleable import User

from app.controllers import ingredient_controller
from app.schemas.ingredient_schema import IngredientCreate, IngredientUpdate, IngredientOut
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.post("/new", response_model=IngredientOut)
async def ingredient_create(ingredient: IngredientCreate, current_user = Depends(get_current_user)):
    return await ingredient_controller.create_ingredient(ingredient)

@router.patch("/{ingredient_id}",response_model=IngredientOut)
async def ingredient_update(ingredient: IngredientUpdate) -> IngredientOut:
    return await ingredient_controller.update_ingredient(ingredient)

@router.get("/all", response_model=list[IngredientOut])
async def ingredient_list():
    return await ingredient_controller.list_ingredients()

@router.delete("/{ingredient_id}",response_model=IngredientOut)
async def ingredient_delete(ingredient_id: int, current_user = Depends(get_current_user)):
    return await ingredient_controller.delete_ingredient(ingredient_id)