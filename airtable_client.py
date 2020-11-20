from dataclasses import asdict
import os

from __init__ import app, config
from airtable import Airtable
from asset import Asset
import requests


class AirtableClient:

    def __init__(self):
        """Initialize AirtableClient."""

        self.airtable_client = Airtable(os.getenv("airtable_base_id"),
                                        config.get("DEFAULT", "table_name"), os.getenv("airtable_api_key"))

    def register_asset(self, asset: Asset):
        """Register to Airtable.

        Register a dictionary with the appropriate key and value to Airtable.

        Args:
            asset (Asset): Asset dataclass with field name of Assets table on AirTable.

        Returns:
            Dictionaries (dict): Dictionary data returned from Airtable.

        """

        try:
            return self.airtable_client.insert(asdict(asset))
        except requests.exceptions.HTTPError as he:
            app.logger.error(he)
            return
