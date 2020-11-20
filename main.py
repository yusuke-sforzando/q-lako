# !/usr/bin/env python3

from flask import render_template, request, session

from __init__ import app
import os
app.secret_key = os.getenv("app_secret_key")


@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.info("index(): GET /")
    template_filename = "index.html"

    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}.",
        "title": "備品・書籍の登録",
        "sub_title": "キーワード、ISBNコード、ASINコードのいずれかを入力してください"
    }
    session["keyword"] = request.form.get("input_keyword")
    return render_template(template_filename, **context_dict)


@ app.route("/search-result", methods=["GET"])
def search_result():
    app.logger.info("search_result(): GET /")
    template_filename = "search-result.html"
    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}."
    }
    return render_template(template_filename, **context_dict, keyword=session["keyword"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
