import pytest

from get_amazon import AmazonGetter


@pytest.fixture
def get_amazon():
    get_amazon = AmazonGetter()
    return get_amazon


def test_search_amazon_with_title(get_amazon):
    """Testing when the equipment name is entered."""

    amazon_search_title = get_amazon.get_search_list("Alexa")
    assert amazon_search_title


def test_search_amazon_with_asin(get_amazon):
    """Testing when the ASIN code is entered."""

    amazon_search_asin = get_amazon.get_search_list("B08BRBFSDR")
    assert amazon_search_asin


def test_search_amazon_with_isbn(get_amazon):
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = get_amazon.get_search_list("9784839966607")
    assert amazon_search_isbn


def test_search_amazon_empty(get_amazon):
    """Testing when an empty keyword is entered."""

    amazon_search_empty = get_amazon.get_search_list("")
    assert not amazon_search_empty


def test_search_amazon_no_exist(get_amazon):
    """Testing when a non-existent value is entered."""

    amazon_search_no_exist = get_amazon.get_search_list("01234567891011121314")
    assert not amazon_search_no_exist
