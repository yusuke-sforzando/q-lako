# !/usr/bin/env python3

from amazon.exception import AmazonException
from flask import request, render_template, url_for, session

from __init__ import app, amazon_api_client
from flash_message import FlashMessage, FlashCategories


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET /{request.full_path}")
    context_dict = {
        "subtitle": "Search results for {{ keyword }}",
        "keyword": request.args.get("query", None)
    }
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
        return FlashMessage.show_with_redirect("Enter any keywords.", FlashCategories.WARNING, url_for("index"))


@ app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        app.logger.info(f"registration: GET {request.full_path}")
        return FlashMessage.show_with_redirect("Enter any keywords.", FlashCategories.WARNING, url_for("index"))
    else:
        app.logger.info(f"registration: POST {request.full_path}")
    app.logger.debug(f"{request.form=}")
    context_dict = {
        "subtitle": "a service that displays detailed information about the item."
    }
    asin = request.form.get("asin", "")
    if asin:
        for product in session["product_list"]:
            if product.asin == asin:
                context_dict["product"] = product
                # TODO: Convert Asset() from product.
    else:
        return render_template("index.html", message="Enter any keywords.")
    return render_template("registration.html", **context_dict)


@app.route("/register_airtable", methods=["POST"])
def resister_airtable():
    app.logger.info("register_airtable(): POST /register_airtable")
    app.logger.debug(f"{request.form=}")
    # TODO: Run `airtable_client.register_asset()`
    if request.form.get("for_test"):  # This line is dummy process
        return FlashMessage.show_with_redirect("Registration completed!", FlashCategories.INFO, url_for("index"))
        # TODO: If registration fails, return to `/registration`
    else:
        context_dict = {
            # TODO: Set asset from `request.form`
            "product": {"title": "Kindle Oasis"}
        }
        return FlashMessage.show_with_render_template("Registration failed.", FlashCategories.ERROR,
                                                      "registration.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
