# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app, amazon_api_client


@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search-result?input_keyword=")
def search_result_direct_access():
    app.logger.info("search_result_direct_access(): GET /")
    return "TOPページに戻ってキーワードを入力してください"


@app.route("/search-result", methods=["GET"])
def search_result():
    app.logger.info("search_result(): GET /")

    keyword = request.args.get("input_keyword", "")
    products_list = []
    search_products_result = amazon_api_client.search_products(keywords=keyword)
    for asset in search_products_result:
        products_list.append({"asin": asset.asin, "title": asset.title, "image_url": asset.images.large})
    print(products_list)
    if keyword:
        return render_template("search-result.html", keyword=keyword)
    else:
        return "TOPページに戻ってキーワードを入力してください"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
