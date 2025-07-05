import pytest
from fixture.driver import HTTPError

VALID_RECIPES = [
    {"title": "No description", "duration": 50, "ingredients": ["Something"]},
    {"title": "With description", "duration": 120, "ingredients": ["onion", "potato"], "description": "Amazing"}
]

INVALID_RECIPES = [
    {"title": "name", "duration": 120, "ingredients": ["Something"]},
    {"title": "Low duration", "duration": 2, "ingredients": ["Something"]},
    {"title": "No ingredients", "duration": 120},
    {"title": "Large duration", "duration": 350, "ingredients": ["Something", "Delicious"]}
]


class TestApp:
    """FastAPI application tests"""

    @pytest.mark.parametrize("recipe", VALID_RECIPES, ids=lambda item: item['title'])
    def test_create_recipe_positive(self, driver, recipe):
        recipe_id = driver.post_recipe(**recipe)
        target_recipe = driver.get_recipe_by_id(recipe_id)
        recipes_list = driver.get_recipes_list()
        assert target_recipe in recipes_list, "Recipe was not created"


    @pytest.mark.parametrize("recipe", INVALID_RECIPES, ids=lambda item: item['title'])
    def test_create_recipe_negative(self, driver, recipe):
        with pytest.raises(HTTPError):
            driver.post_recipe(**recipe)



