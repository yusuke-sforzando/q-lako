import os

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
    assert os.getenv("airtable_base_id")
    assert os.getenv("airtable_api_key")
    assert os.getenv("amazon_partner_tag")
    assert os.getenv("amazon_access_key")
    assert os.getenv("amazon_secret_key")
