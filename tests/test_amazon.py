import os

from __init__ import amazon_api_client


def test_api_keys():
    assert os.getenv("amazon_partner_tag")
    assert os.getenv("amazon_access_key")
    assert os.getenv("amazon_secret_key")


def test_search_amazon_with_title():
    """Testing when the equipment name is entered."""

    amazon_search_title = amazon_api_client.search_products(keywords="PS5")
    assert amazon_search_title


def test_search_amazon_with_asin():
    """Testing when the ASIN code is entered."""

    amazon_search_asin = amazon_api_client.search_products(keywords="B08BRBFSDR")
    assert amazon_search_asin


def test_search_amazon_with_isbn():
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = amazon_api_client.search_products(keywords="9784839966607")
    assert amazon_search_isbn


def test_search_amazon_no_product():
    """Testing when a non-existent value is entered."""

    search_no_exist = amazon_api_client.search_products(keywords="01234567891011121314")
    assert not search_no_exist
