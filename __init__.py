from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

app = Flask(__name__)


if os.getenv("GAE_ENV", "").startswith("standard"):
    """ Production in GAE """
    app.config["IS_LOCAL"] = False
    import google.cloud.logging
    from google.cloud.logging.handlers import CloudLoggingHandler
    import logging

    client = google.cloud.logging.Client()
    handler = CloudLoggingHandler(client)
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
