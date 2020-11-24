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


@app.route("/registration", methods=["GET", "POST"])
def registration():
    app.logger.info("search(): POST /registration")
    asin = "B07XB5WX89"
    product = amazon_api_client.search_products(keywords=asin)[0]
    contributors = product.info.contributors
    context_dict = {
        "subtitle": "registration details",
        "asin": asin,
        "product": product,
        "contributors": "None"
    }
    if contributors:
        context_dict["contributors"] = [contributor.name for contributor in contributors]
    return render_template("registration.html", **context_dict)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8888)
