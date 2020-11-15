# !/usr/bin/env python3

# Start preliminary injunction

from amazon.paapi import AmazonAPI
from dotenv import load_dotenv
import os

load_dotenv()


class Amazon:
    amazon_partner_tag = os.getenv("amazon_partner_tag")
    amazon_access_key = os.getenv("amazon_access_key")
    amazon_secret_key = os.getenv("amazon_secret_key")
    key = os.getenv("amazon_secret_key")
# End preliminary injunction


class GetAmazonList:
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
            products :
        """

        amazon = AmazonAPI(Amazon.amazon_access_key, Amazon.amazon_secret_key,
                           Amazon.amazon_partner_tag, "JP")
        self.products = amazon.search_items(item_count=self.item_count, keywords=self.search_word)
        for product in self.products["data"]:
            title = product.item_info.title.display_value
            url = product.detail_page_url
            try:
                image_url = product.images.primary.medium.url
            except AttributeError:
                image_url = "None"
            self.amazon_list.append({"Title": title, "url": url, "image_url": image_url})


if __name__ == "__main__":
    # amazon_list = GetAmazonList("B087QZ1FWZ").amazon_list
    amazon_list = GetAmazonList("PS5").amazon_list

    for product in amazon_list:
        print(product)
