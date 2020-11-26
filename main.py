# !/usr/bin/env python3

from flask import request, render_template, url_for

from __init__ import app, flash_message
from flash_message import FlashCategories


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET {request.full_path}")
    keyword = request.args.get("query", None)
    if keyword:
        context_dict = {
            "subtitle": f"Search Result for {keyword}",
            "keyword": keyword,
        }
        return render_template("search.html", **context_dict)
    else:
        return flash_message.show_with_redirect("Enter any keywords.", FlashCategories.WARNING, url_for("index"))


@app.route("/register_airtable", methods=["POST"])
def resister_airtable():
    app.logger.info("register_airtable(): POST /register_airtable")
    app.logger.debug(f"{request.form=}")
    # TODO: Run `airtable_client.register_asset()`.
    if request.form.get("for_test"):  # This line is dummy process.
        return flash_message.show_with_redirect("Registration completed!", FlashCategories.INFO, url_for("index"))
    # TODO: If registration fails, return to `/registration`.
    else:
        context_dict = {
            # TODO: set asset from `request.form`.
            "asset": {"title": "Kindle Oasis"}
        }
        return flash_message.show_with_render_template("Registration failed.", FlashCategories.ERROR,
                                                       "registration.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
