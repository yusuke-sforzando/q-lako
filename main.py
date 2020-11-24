# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app, amazon_api_client
from asset import Asset


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    template_filename = "index.html"
    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}."
    }
    return render_template(template_filename, **context_dict)


@app.route("/registration", methods=["GET"])
def registration():
    if request.method == "GET":
        app.logger.info(f"registration(): GET {request.full_path}")
    asin = request.form.get("asin", "B07XB5WX89")

    product = amazon_api_client.search_products(keywords=asin)[0]

    registerable_asset = Asset(
        title=product.title,
        asin=product.asin,
        url=product.url,
        images=product.images.large,
        manufacture=product.info.manufacturer,
        contributor="",
        product_group=product.info.product_group,
        publication_date=product.info.publication_date,
        features=product.product.features,
        default_position="",
        current_position="",
        note="",
        registrant_name="")

    contributors = product.info.contributors
    context_dict = {
        "subtitle": "registration details",
        "asin": registerable_asset.asin,
        "contributors": "None",
        "registerable_asset": registerable_asset
    }
    if contributors:
        context_dict["contributors"] = [contributor.name for contributor in contributors]
    return render_template("registration.html", **context_dict)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8888)
