import pytest

from __init__ import amazon
from main import app
import os


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


def test_search_amazon_with_title():
    """Testing when the equipment name is entered."""

    amazon_search_title = amazon.search_products(keywords="B08BRBFSDR")
    assert amazon_search_title


def test_search_amazon_with_asin():
    """Testing when the ASIN code is entered."""

    amazon_search_asin = amazon.search_products(keywords="B08BRBFSDR")
    assert amazon_search_asin


def test_search_amazon_with_isbn():
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = amazon.search_products(keywords="9784839966607")
    assert amazon_search_isbn


def test_search_amazon_no_product():
    """Testing when a non-existent value is entered."""

    search_no_exist = amazon.search_products(keywords="01234567891011121314")
    assert not search_no_exist
