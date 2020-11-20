from configparser import ConfigParser
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
import os

from __init__ import app
from airtable import Airtable
import requests


config = ConfigParser()

config.read("settings.ini", encoding="utf8")
table_name = config.get("DEFAULT", "table_name")


@dataclass
class AirTable:

    title: str
    asin: str
    url: str
    images: list
    manufacture: str
    contributor: str
    product_group: str
    publication_date: str
    features: str
    default_position: str
    current_position: str
    note: str
    registrant_name: str
    registered_at: str


class AirtableClient:

    def __init__(self):
        """Initialize AirtableClient."""

        self.airtable_client = Airtable(os.getenv("airtable_base_id"), table_name, os.getenv("airtable_api_key"))

    def register_assets(self, AirTable):
        """Register to Airtable.

        Register to Airtable, taking as an argument a dictionary
        with key names and elements corresponding to the Airtable table.

        Args:
            registerable_dictionary (dict): A dictionary with key names to the Airtable table.

        Returns:
            registerable_dictionary (dict): If the registration is successful,
                                            the registered dictionary will be returned.

        """
        registerable_dictionary = asdict(AirTable)
        time_now = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=+9)))
        registerable_dictionary["registered_at"] = time_now.isoformat()
        try:
            return self.airtable_client.insert(registerable_dictionary)
        except requests.exceptions.HTTPError as he:
            app.logger.error(he)
