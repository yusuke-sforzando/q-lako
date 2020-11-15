# !/usr/bin/env python3

from amazon.paapi import AmazonAPI
import api_keys


class AmazonListGetter:
    """Get a list of Amazon's search results."""

    def __init__(self, search_word: str, item_count=3):
        """Initialize GetAmazonList."""
        self.amazon_list = []
        self.search_word = search_word
        self.item_count = item_count
        self.get_search_list()

    def get_search_list(self):
        """Get the search list.

            Retrieves a list of search results with any URL,
            product name and ASIN/ISBN code as arguments.

        Returns:
            products (list): List of Amazon items (from 1 to 30).
        """

        amazon = AmazonAPI(api_keys.amazon_access_key, api_keys.amazon_secret_key,
                           api_keys.amazon_partner_tag, "JP")
        self.products = amazon.search_items(item_count=self.item_count, keywords=self.search_word)
        for product in self.products["data"]:
            title = product.item_info.title.display_value
            url = product.detail_page_url
            try:
                image_url = product.images.primary.medium.url
            except AttributeError:
                image_url = "None"
            self.amazon_list.append({"Title": title, "url": url, "image_url": image_url})
