import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert b"This is index.html" in response.data
    assert response.status_code == 200


def test_api_keys():
    assert api_keys.airtable_base_id
    assert api_keys.airtable_api_key
    assert api_keys.amazon_partner_tag
    assert api_keys.amazon_access_key
    assert api_keys.amazon_secret_key
