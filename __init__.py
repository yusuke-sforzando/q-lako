import os
from configparser import ConfigParser
from pathlib import Path

from amazon.paapi import AmazonAPI
from dotenv import load_dotenv
from flask import Flask

load_dotenv(verbose=True)
config_parser = ConfigParser()
config_parser.read("settings.ini", encoding="utf8")

app = Flask(__name__)
app.config["AIRTABLE_TABLE_NAME"] = config_parser.get("Airtable", "airtable_table_name")

amazon_api_client = AmazonAPI(os.getenv("amazon_access_key"),
                              os.getenv("amazon_secret_key"),
                              os.getenv("amazon_partner_tag"),
                              "JP")

if os.getenv("GAE_ENV", "").startswith("standard"):
    """ Production in GAE """

    app.config["IS_LOCAL"] = False
    import google.cloud.logging
    import logging

    client = google.cloud.logging.Client()
    handler = client.get_default_handler()
    cloud_logger = logging.getLogger(__name__)
    cloud_logger.setLevel(logging.DEBUG)
    cloud_logger.addHandler(handler)
else:
    """ Local execution """

    app.config["IS_LOCAL"] = True
    app.debug = True

    try:
        import flask_monitoringdashboard as dashboard

        dashboard.bind(app)
    except ImportError as ie:
        app.logger.warning(f"{ie}")

# Read theme color form settings.ini
app.config["THEME_COLOR"] = config_parser.get("Common", "theme_color_gray")

# Update css with theme color in settings.ini
css_dir = Path("static/css")
os.makedirs(css_dir, exist_ok=True)
css_file_path = css_dir / "common.css"
with open(css_file_path, mode="r") as rf:
    css_lines = rf.readlines()
    for index, line in enumerate(css_lines):
        if "theme-color-blue" in line:
            css_lines[index + 1] = f"  color: {config_parser.get('Common', 'theme_color_blue')};\n"
        elif "theme-color-gray" in line:
            css_lines[index + 1] = f"  color: {app.config['THEME_COLOR']};\n"
        elif "theme-bg-color-gray" in line:
            css_lines[index + 1] = f"  background-color: {app.config['THEME_COLOR']};\n"
with open(css_file_path, mode="w") as wf:
    wf.writelines(css_lines)
