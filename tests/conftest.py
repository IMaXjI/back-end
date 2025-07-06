import pytest
from src.main import app
from fixture.driver import RecipeDriver


@pytest.fixture(scope='session')
def driver():
    with RecipeDriver(app) as _driver:
        yield _driver

