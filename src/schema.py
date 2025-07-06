from typing import List, Optional
from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    """Recipe base structure"""
    title: str = Field(
        ...,
        min_length=5,
        max_length=40
    )
    duration: int = Field(
        ...,
        title="Cooking duration in minutes",
        ge=5,
        le=300
    )
    ingredients: List[str]
    description: Optional[str] = None


class RecipeIn(RecipeBase):
    ...


class RecipeOut(RecipeBase):
    id: int
    views: int

    class Config:
        orm_mode = True
