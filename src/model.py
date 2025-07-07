from src.db import Database
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy import Column, Integer, String

Base = Database.get_declarative_base()


class Recipe(Base):
    """Recipes aggregation table"""

    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    views = Column(Integer, default=0, index=True)
    title = Column(String, index=True, nullable=False)
    duration = Column(Integer, index=True, nullable=False)
    ingredients = Column(JSON, index=True, nullable=False)
    description = Column(String, index=True)


