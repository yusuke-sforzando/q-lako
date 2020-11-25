# !/usr/bin/env python3

from amazon.exception import AmazonException
from flask import render_template, request, session

from __init__ import app, amazon_api_client


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    template_filename = "index.html"
    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}."
    }
    return render_template(template_filename, **context_dict)


@app.route("/search", methods=["GET", "POST"])
def search():
    keyword = request.args.get("query", "")
    context_dict = {
        "subtitle": "a service that displays search results."
    }
    app.logger.info(f"saerch(): GET /{request.full_path}")
    if keyword:
        context_dict["keyword"] = keyword

        try:
            product_list = amazon_api_client.search_products(keywords=keyword)
            item_hits = len(product_list)
            context_dict["product_list"] = product_list
            context_dict["item_hits"] = item_hits
            session["product_list"] = product_list[0].title
        except AmazonException as ae:
            app.logger.error(f"{ae}")
            raise ae
    else:
        context_dict["message"] = "Enter keywords back on the top page."
    return render_template("search.html", **context_dict)


@ app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        app.logger.info(f"search(): GET /{request.full_path}")
    elif request.method == "POST":
        app.logger.info(f"search(): POST /{request.full_path}")

    asin = request.form.get("asin", "")
    context_dict = {
        "subtitle": "a service that displays detailed information about the item."
    }
    if asin:
        context_dict["asin"] = asin
    else:
        context_dict["message"] = "Enter keywords back on the top page."
    print(session["product_list"])
    return render_template("registration.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
