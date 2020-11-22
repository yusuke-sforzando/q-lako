# !/usr/bin/env python3

from flask import render_template, request

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


@app.route("/search", methods=["GET"])
def search():
    app.logger.info("search(): GET /search")
    products_list = []
    keyword = request.args.get("query", "")
    search_products_result = amazon_api_client.search_products(keywords=keyword)
    for product in search_products_result:
        products_list.append({"asin": product.asin, "title": product.title, "image_url": product.images.large})
    context_dict = {
        "keyword": keyword,
        "products_list": products_list
    }
    return render_template("search.html", **context_dict)


@app.route("/registration-details", methods=["GET"])
def registration_details():
    app.logger.info("search(): GET /registration-details")
    asin = request.args.get("asin")
    return render_template("registration-details.html", asin=asin)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
