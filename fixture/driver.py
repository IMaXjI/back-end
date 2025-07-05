from typing import List, Optional
from requests import Response, HTTPError
from fastapi.testclient import TestClient


class RecipeDriver(TestClient):
    """Recipes API driver"""

    @classmethod
    def _verify_response(cls, response: Response) -> bool:
        if response.status_code in range(400):
            return True
        raise HTTPError("Request error occurred. Response:", response.text)

    def get_recipes_list(self) -> List[dict]:
        response = self.get("/recipes")
        if self._verify_response(response):
            return response.json()

    def get_recipe_by_id(self, recipe_id: int) -> dict:
        response = self.get(f"/recipes/{recipe_id}")
        if self._verify_response(response):
            return response.json()

    def post_recipe(self, title: Optional[str] = None, duration: Optional[int] = None,
                    ingredients: Optional[List[str]] = None, description: Optional[str] = None) -> int:
        payload = {
            "title": title,
            "duration": duration,
            "ingredients": ingredients,
            "description": description
        }
        response = self.post("/recipes", json=payload)
        if self._verify_response(response):
            recipe_id = response.json()["id"]
            return recipe_id

    def destroy(self):
        self.close()
