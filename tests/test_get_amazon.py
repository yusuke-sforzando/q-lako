from get_amazon import AmazonListGetter


def test_search_amazon_title():
    amazon_search_title = AmazonListGetter("Alexa").amazon_list
    assert amazon_search_title


def test_search_amazon_asin():
    amazon_search_asin = AmazonListGetter("B08BRBFSDR").amazon_list
    assert amazon_search_asin


def test_search_amazon_isbn():
    amazon_search_isbn = AmazonListGetter("9784839966607").amazon_list
    assert amazon_search_isbn
