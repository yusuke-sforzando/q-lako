# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET {request.full_path}")
    keyword = request.args.get("query", "")
    context_dict = {
        "subtitle": "search result",
        "keyword": keyword
    }
    if not keyword:
        context_dict["message"] = "TOPページに戻ってキーワードを入力してください"

    return render_template("search.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
