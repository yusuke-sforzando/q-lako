# !/usr/bin/env python3

from amazon.paapi import AmazonAPI
from amazon.paapi import AmazonException
import os

from __init__ import app


class AmazonGetter:
    """Get search results from Amazon."""

    def __init__(self):
        """Initialize GetAmazonList."""
        self.amazon = AmazonAPI(os.getenv("amazon_access_key"), os.getenv("amazon_secret_key"),
                                os.getenv("amazon_partner_tag"), "JP")

    def get_search_list(self, keyword: str, item_count=30):
        """Get the search list.

            Retrieves a list of search results with any URL,
            product name and ASIN/ISBN code as arguments.
        Args:
            keyword (str): The product name or code you want to search for on Amazon.
            item_count (int): The number of items you want to search for at a time.

        Returns:
            products (list): List of Amazon items.
        """

        try:
            products = self.amazon.search_items(keywords=keyword, item_count=item_count)
        except AmazonException as e:
            print("No results found for your request", e)
            return []

        product_list = []
        for product in products["data"]:
            product = product.to_dict()
            image_url = product["images"]["primary"]["large"]["url"] if product.get("images") else "None"
            product_list.append({"ASIN": product["asin"], "Title": product["item_info"]["title"]
                                 ["display_value"], "url": product["detail_page_url"], "image_url": image_url})
        return product_list

    def get_search_detail(self, asin_code: str):
        """Get the search item detail.

            Retrieves a list of search results with any URL,
            product name and ASIN/ISBN code as arguments.
        Args:
            keyword (str): The product name or code you want to search for on Amazon.
            item_count (int): The number of items you want to search for at a time.

        Returns:
            products (list): List of Amazon items.
        """

        try:
            product = self.amazon.get_items(item_ids=[asin_code])
        except AmazonException as e:
            print("No results found for your request", e)
            return []
        print(asin_code)
        return product
        # product_list = []
        # for product in products["data"]:
        #     product = product.to_dict()
        #     image_url = product["images"]["primary"]["large"]["url"] if product.get("images") else "None"
        #     product_list.append({"ASIN": product["asin"], "Title": product["item_info"]["title"]
        #                          ["display_value"], "url": product["detail_page_url"], "image_url": image_url})
        # return product_list


if __name__ == "__main__":
    product = AmazonGetter().get_search_detail("B081T9Z4KG")
    import pprint
    pprint.pprint(product)
