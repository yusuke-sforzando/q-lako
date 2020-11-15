# !/usr/bin/env python3

from dotenv import load_dotenv
import os

load_dotenv()

airtable_base_id = os.getenv("airtable_base_id")
airtable_api_key = os.getenv("airtable_api_key")
amazon_partner_tag = os.getenv("amazon_partner_tag")
amazon_access_key = os.getenv("amazon_access_key")
amazon_secret_key = os.getenv("amazon_secret_key")
