# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info("search(): GET /search")
    keyword = request.args.get("query", "")
    template_filename = "search.html"
    context_dict = {
        "subtitle": template_filename,
        "keyword": keyword
    }
    if not keyword:
        context_dict["message"] = "TOPページに戻ってキーワードを入力してください"

    return render_template(template_filename, **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
