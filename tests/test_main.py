import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_search(test_client):
    response = test_client.get("/search?query=サーカスTC")
    assert b"search.html" in response.data
    assert response.status_code == 200


def test_GET_registration_details(test_client):
    response = test_client.get("/registration-details?asin=B07B7HG86W")
    assert b"registration-details.html" in response.data
    assert response.status_code == 200
