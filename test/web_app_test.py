import pytest
from bs4 import BeautifulSoup

from web_app import create_app

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()


def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

def test_meal(test_client):
    response = test_client.get("/meal")
    assert response.status_code == 200
    assert b"""<p>No meals found.</p>""" in response.data


def test_recipe(test_client):
    response = test_client.get("/meal/52956")
    assert response.status_code == 200

    assert b"""<div class="container mt-4">
    <h2 class="mb-3">Chicken Congee</h2>""" in response.data