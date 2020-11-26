# !/usr/bin/env python3

from amazon.exception import AmazonException
from flask import render_template, request, session

from __init__ import app, amazon_api_client
from asset import Asset


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    context_dict = {
        "subtitle": "Registration of equipment and books",
        "message": "Enter one of the following keywords: keyword, ISBN code, or ASIN code"
    }
    return render_template("index.html", **context_dict)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        app.logger.info(f"search(): GET /{request.full_path}")
    elif request.method == "POST":
        app.logger.info(f"search(): POST /{request.full_path}")
    context_dict = {
        "subtitle": "a service that displays search results."
    }
    keyword = request.args.get("query", "")

    if keyword:
        context_dict["keyword"] = keyword
        try:
            product_list = amazon_api_client.search_products(keywords=keyword)
            item_hits = len(product_list)
            asset_list = []
            for product in product_list:
                asset_list.append(
                    Asset(
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
                        registrant_name=""
                    )
                )
            session["asset_list"] = asset_list
            context_dict["asset_list"] = asset_list
            context_dict["item_hits"] = item_hits
        except AmazonException as ae:
            app.logger.error(f"{ae}")
            raise ae
    else:
        context_dict["message"] = "Enter any keywords."
    return render_template("search.html", **context_dict)


@ app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        app.logger.info(f"registration: GET /{request.full_path}")
    elif request.method == "POST":
        app.logger.info(f"registration: POST /{request.full_path}")
    context_dict = {
        "subtitle": "a service that displays detailed information about the item."
    }
    asin = request.form.get("asin", "")
    if asin:
        for asset in session.get("asset_list", ""):
            if asset.asin == asin:
                context_dict["asin"] = asset.asin
    else:
        context_dict["message"] = "Enter any keywords."
    return render_template("registration.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
