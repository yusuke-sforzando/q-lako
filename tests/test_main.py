import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Registration of equipment and books." in response.data
    assert b"Enter one of the following keywords" in response.data


def test_GET_search_with_correct_query(test_client):
    response = test_client.get("/search?query=kindle")
    assert b"kindle" in response.data


def test_GET_search_with_incorrect_query(test_client):
    response = test_client.get("/search?unexpected_query=kindle", follow_redirects=True)
    assert b"Enter any keywords." in response.data


def test_GET_search_with_not_inputted_query(test_client):
    response = test_client.get("/search?query=", follow_redirects=True)
    assert b"a service to quickly register equipments and books." in response.data
    assert b"Enter any keywords." in response.data


def test_GET_search_direct_access(test_client):
    response = test_client.get("/search", follow_redirects=True)
    assert b"Enter any keywords." in response.data


def test_POST_register_airtable_success(test_client):
    response = test_client.post("/register_airtable", data={"for_test": True}, follow_redirects=True)
    assert b"Registration of equipment and books." in response.data
    assert b"Registration completed!" in response.data


def test_POST_register_airtable_failure(test_client):
    response = test_client.post("/register_airtable", data={"for_test": None}, follow_redirects=True)
    assert b"Asset details" in response.data
    assert b"Title: Kindle Oasis" in response.data
    assert b"Registration failed." in response.data
