# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app


@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.info("index(): GET /")
    template_filename = "index.html"

    context_dict = {
        "subtitle": template_filename,
        "message": f"This is {template_filename}.",
        "title": "備品・書籍の登録",
        "sub_title": "キーワード、ISBNコード、ASINコードのいずれかを入力してください",
        "keyword": request.form.get("input_keyword")
    }
    return render_template(template_filename, **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
