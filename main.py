# !/usr/bin/env python3

from flask import render_template

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


@app.route("/search-result", methods=["GET"])
def search():
    app.logger.info("search(): GET /search-result")

    keyword = "PlayStation5"
    products_list = []
    search_products_result = amazon_api_client.search_products(keywords=keyword)
    for product in search_products_result:
        products_list.append({"asin": product.asin, "title": product.title, "image_url": product.images.large})
    return render_template("search-result.html", keyword=keyword, products_list=products_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
