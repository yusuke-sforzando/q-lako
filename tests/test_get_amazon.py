from get_amazon import FetchAmazon


def test_search_amazon_with_title():
    """Testing when the equipment name is entered."""

    amazon_search_title = FetchAmazon("Alexa").amazon_list
    assert amazon_search_title


def test_search_amazon_with_asin():
    """Testing when the ASIN code is entered."""

    amazon_search_asin = FetchAmazon("B08BRBFSDR").amazon_list
    assert amazon_search_asin


def test_search_amazon_with_isbn():
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = FetchAmazon("9784839966607").amazon_list
    assert amazon_search_isbn


def test_search_amazon_no_exist():
    """Testing when a non-existent value is entered."""

    amazon_search_no = FetchAmazon("").amazon_list
    assert not amazon_search_no
