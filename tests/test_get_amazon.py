from get_amazon import AmazonGetter


def test_search_amazon_with_title():
    """Testing when the equipment name is entered."""

    amazon_search_title = AmazonGetter().get_search_list("Alexa")
    assert amazon_search_title


def test_search_amazon_with_asin():
    """Testing when the ASIN code is entered."""

    amazon_search_asin = AmazonGetter().get_search_list("B08BRBFSDR")
    assert amazon_search_asin


def test_search_amazon_with_isbn():
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = AmazonGetter().get_search_list("9784839966607")
    assert amazon_search_isbn


def test_search_amazon_empty():
    """Testing when an empty keyword is entered."""

    amazon_search_empty = AmazonGetter().get_search_list("")
    assert not amazon_search_empty


def test_search_amazon_no_exist():
    """Testing when a non-existent value is entered."""

    amazon_search_no_exist = AmazonGetter().get_search_list("0123456781011121314")
    assert not amazon_search_no_exist
