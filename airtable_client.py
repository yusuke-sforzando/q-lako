from configparser import ConfigParser
from dataclasses import asdict
import os

from __init__ import app
from airtable import Airtable
from airtable_data import AirtableDataClass
import requests


config = ConfigParser()

config.read("settings.ini", encoding="utf8")
table_name = config.get("DEFAULT", "table_name")


class AirtableClient:

    def __init__(self):
        """Initialize AirtableClient."""

        self.airtable_client = Airtable(os.getenv("airtable_base_id"), table_name, os.getenv("airtable_api_key"))

    def register_assets(self, register_assets: AirtableDataClass):
        """Register to Airtable.

        Register to Airtable, taking as an argument AirTable class
        with key names corresponding to the Airtable table.

        Args:
            AirTable (AirTable class): AirTable class with the Airtable field name.

        Returns:
            registerable_dictionary (dict): If the registration is successful,
                                            the registered dictionary will be returned.

        """
        registerable_dictionary = asdict(register_assets)
        try:
            return self.airtable_client.insert(registerable_dictionary)
        except requests.exceptions.HTTPError as he:
            app.logger.error(he)
            return
