# !/usr/bin/env python3

import os

from airtable import Airtable


class AirtableClient:
    def __init__(self):
        self.airtable_client = Airtable(os.getenv("airtable_base_id"), "q-lako", os.getenv("airtable_api_key"))

    def register_table(self, airtable_dict: dict):
        self.airtable_client.insert(airtable_dict)
