from dataclasses import asdict
import os

from __init__ import app, config
from airtable import Airtable
from assets import Assets
import requests


class AirtableClient:

    def __init__(self):
        """Initialize AirtableClient."""

        self.airtable_client = Airtable(os.getenv("airtable_base_id"),
                                        config.get("DEFAULT", "table_name"), os.getenv("airtable_api_key"))

    def register_assets(self, register_assets: Assets):
        """Register to Airtable.

        Register to Airtable, taking as an argument register_assets
        with key names corresponding to the Airtable table.

        Args:
            register_assets (AirtableDataClass class): AirTable class with the Airtable field name.

        Returns:
            Dictionaries (dict): Dictionary data returned from Airtable.

        """

        try:
            return self.airtable_client.insert(asdict(register_assets))
        except requests.exceptions.HTTPError as he:
            app.logger.error(he)
            return
