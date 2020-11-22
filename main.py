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
    template_filename = "registration-details.html"
    asin = request.args.get("query", "")
    product = amazon_api_client.search_products(keywords=asin)[0]
    context_dict = {
        "subtitle": template_filename,
        "product": product,
        "template_file": template_filename,
        "contributors": [contributor for contributor in product.info.contributors]
    }
    print(context_dict["contributors"])
    return render_template("registration-details.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
