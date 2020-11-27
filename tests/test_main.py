import pytest

import flask
from main import app

with app.test_request_context('/'):
    assert flask.request.path == '/'


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Registration of equipment and books." in response.data
    assert b"Enter one of the following keywords: keyword, ISBN code, or ASIN code." in response.data


def test_GET_search_with_correct_query(test_client):
    response = test_client.get("/search?query=kindle")
    assert b"kindle" in response.data


def test_GET_search_with_incorrect_query(test_client):
    response = test_client.get("/search?unexpected_query=kindle")
    assert b"Enter any keywords." in response.data


def test_GET_search_with_not_inputted_query(test_client):
    response = test_client.get("/search?query=")
    assert b"Enter any keywords." in response.data


def test_GET_search_direct_access(test_client):
    response = test_client.get("/search")
    assert b"Enter any keywords." in response.data


def test_GET_registration_direct_access(test_client):
    response = test_client.get("/registration")
    assert b"Enter any keywords." in response.data


def test_GET_registration_asin(test_client):
    test_client.get("/search?query=サーカスTC")
    response = test_client.post("/registration", data={"asin": "B07XB5WX89"})
    assert b"B07XB5WX89" in response.data
