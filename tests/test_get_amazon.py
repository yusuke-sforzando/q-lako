from get_amazon import SearchAmazonList


def test_search_amazon_title():
    """Testing when the equipment name is entered."""

    amazon_search_title = SearchAmazonList("Alexa").amazon_list
    assert amazon_search_title


def test_search_amazon_asin():
    """Testing when the ASIN code is entered."""

    amazon_search_asin = SearchAmazonList("B08BRBFSDR").amazon_list
    assert amazon_search_asin


def test_search_amazon_isbn():
    """Testing when the ISBN code is entered."""

    amazon_search_isbn = SearchAmazonList("9784839966607").amazon_list
    assert amazon_search_isbn


def test_search_amazon_no():
    """Testing when a non-existent value is entered."""

    amazon_search_no = SearchAmazonList("9784839966607asadAASSSSSS").amazon_list
    assert not amazon_search_no
