# !/usr/bin/env python3

from amazon.paapi import AmazonAPI
from amazon.paapi import AmazonException

import os


class FetchAmazon:
    """Get search results from Amazon."""

    def __init__(self, search_word: str, item_count=3):
        """Initialize GetAmazonList."""
        self.amazon_list = []
        self.search_word = search_word
        self.item_count = item_count
        self.amazon = AmazonAPI(os.getenv("amazon_access_key"), os.getenv("amazon_secret_key"),
                                os.getenv("amazon_partner_tag"), "JP")
        self.get_search_list()

    def get_search_list(self):
        """Get the search list.

            Retrieves a list of search results with any URL,
            product name and ASIN/ISBN code as arguments.

        Returns:
            products (list): List of Amazon items (from 1 to 30).
        """

        try:
            self.products = self.amazon.search_items(item_count=self.item_count, keywords=self.search_word)
            for product in self.products["data"]:
                title = product.item_info.title.display_value
                url = product.detail_page_url
                try:
                    image_url = product.images.primary.medium.url
                    self.amazon_list.append({"Title": title, "url": url, "image_url": image_url})
                except AttributeError as e:
                    print("image_url is not exist", e)
                    self.amazon_list.append({"Title": title, "url": url, "image_url": ""})
        except AmazonException as e:
            print("No results found for your request", e)
            self.amazon_list = []
