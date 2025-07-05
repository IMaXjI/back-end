from src import model
from src import schema
from src.db import Database
from fastapi import APIRouter
from sqlalchemy import select, update
from typing import List, Union, Optional


router = APIRouter()
session = Database.get_session()


@router.post("/recipes", response_model=schema.RecipeOut)
async def recipes(recipe: schema.RecipeIn) -> model.Recipe:
    new_recipe = model.Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@router.get("/recipes", response_model=List[schema.RecipeOut])
@router.get("/recipes/{idx}", response_model=schema.RecipeOut)
async def recipes(idx: Optional[int] = None) -> Union[List[model.Recipe], model.Recipe]:
    async with session.begin():
        if idx:
            await session.execute(
                update(model.Recipe)
                .where(model.Recipe.id == idx)
                .values(views=model.Recipe.views + 1)
            )
            result = await session.execute(
                select(model.Recipe)
                .where(model.Recipe.id == idx)
            )
            return result.scalar_one_or_none()
        else:
            result = await session.execute(
                select(model.Recipe)
                .order_by(model.Recipe.views.desc())
                .order_by(model.Recipe.duration)
            )
            return result.scalars().all()
