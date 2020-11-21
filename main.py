# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app, amazon_api_client


@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info("search(): GET /search")

    keyword = "PS5"
    products_list = []
    search_products_result = amazon_api_client.search_products(keywords=keyword)
    for product in search_products_result:
        products_list.append({"asin": product.asin, "title": product.title, "image_url": product.images.large})
    print(products_list)
    if keyword:
        return render_template("search.html", keyword=keyword, products_list=products_list)
    else:
        return "TOPページに戻ってキーワードを入力してください"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
