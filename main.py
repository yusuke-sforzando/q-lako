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


@app.route("/registration-details", methods=["GET"])
def registration_details():
    app.logger.info("search(): GET /registration-details")
    asin = "B07B7HG86W"
    products = amazon_api_client.search_products(keywords=asin)
    product = products[0].asin
    print(product)
    return render_template("registration-details.html", prpduct=product)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
