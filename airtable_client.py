# !/usr/bin/env python3

from configparser import ConfigParser
from datetime import datetime, timezone, timedelta
import os

from airtable import Airtable
import requests


config = ConfigParser()

config.read("settings.ini", encoding="utf8")
table_name = config.get("DEFAULT", "table_name")


class AirtableClient:
    def __init__(self):
        """Initialize AirtableClient."""

        self.table_columns = config.get("DEFAULT", "table_columns").split(",")
        self.airtable_client = Airtable(os.getenv("airtable_base_id"), table_name, os.getenv("airtable_api_key"))

    def validate_input_dict(self, unverified_dict):
        """Validate that the input dictionary holds the proper key names.

        To check if the entered dictionary has a key name that corresponds to the field name of Airtable.
        Dictionaries to be registered in airtable must have the following key values.


        Args:
            unverified_dict (dict): Dictionary to check if it can be registered to Airtable.

        Returns:
            bool: Returns True if it held the appropriate key value, False if it did not.

        """

        airtable_field = self.airtable_client.get_all(maxRecords=1)[0]["fields"]
        return set(airtable_field.keys()) == set(unverified_dict.keys())

    def register_assets(self, registerable_dictionary: dict):
        """Register to Airtable.

        Register to Airtable,taking as an argument a dictionary
        with key names and elements corresponding to the Airtable table.

        Args:
            registerable_dictionary (dict): A dictionary with key names to the Airtable table.

        Returns:
            registerable_dictionary (dict): If the registration is successful,
                                            the registered dictionary will be returned.
            HTTPError responce (str): All exceptions inherit from requests.exceptions.
                                      RequestException and are raised explicitly.

        """
        time_now = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=+9)))
        registerable_dictionary["registered_at"] = time_now.isoformat()
        try:
            return self.airtable_client.insert(registerable_dictionary)
        except requests.exceptions.HTTPError as he:
            return he
