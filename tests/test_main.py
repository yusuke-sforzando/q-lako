import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert b"This is dummy message." in response.data
    assert response.status_code == 200


def test_GET_registration(test_client):
    response = test_client.get("/registration")
    assert b"registration details" in response.data
    assert response.status_code == 200
