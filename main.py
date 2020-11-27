# !/usr/bin/env python3

from amazon.exception import AmazonException
from flask import render_template, request, session

from __init__ import app, amazon_api_client


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET /{request.full_path}")
    context_dict = {
        "subtitle": "Search results for {{ keyword }}",
        "keyword": request.args.get("query", "")
    }
    if session.get("product_list", ""):
        context_dict["product_list"] = session["product_list"]
        context_dict["item_hits"] = len(session["product_list"])
        return render_template("search.html", **context_dict)
    if context_dict["keyword"]:
        try:
            session["product_list"] = amazon_api_client.search_products(keywords=context_dict["keyword"])
            context_dict["product_list"] = session["product_list"]
            context_dict["item_hits"] = len(session["product_list"])

        except AmazonException as ae:
            app.logger.error(f"{ae}")
            raise ae
        return render_template("search.html", **context_dict)

    else:
        context_dict["message"] = "Enter any keywords."
        return render_template("index.html", **context_dict)


@ app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        app.logger.info(f"registration: GET /{request.full_path}")
        return render_template("index.html", message="Enter any keywords.")
    else:
        app.logger.info(f"registration: POST /{request.full_path}")
    context_dict = {
        "subtitle": "a service that displays detailed information about the item."
    }
    asin = request.form.get("asin", "")
    if asin:
        for product in session["product_list"]:
            if product.asin == asin:
                context_dict["asin"] = product.asin
                # TODO: Convert Asset() from product.
    else:
        return render_template("index.html", message="Enter any keywords.")
    return render_template("registration.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
