# !/usr/bin/env python3

from flask import render_template

from __init__ import app

import os


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    template_filename = "index.html"
    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}."
    }
    return render_template(template_filename, **context_dict)


if __name__ == "__main__":
    print(os.getenv("airtable_base_id"))
    app.run(host="0.0.0.0", port=8888)
