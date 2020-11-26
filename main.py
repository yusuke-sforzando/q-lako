# !/usr/bin/env python3

from flask import render_template, request

from __init__ import app

app.secret_key = "aasss"


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
<<<<<<< HEAD
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET {request.full_path}")
    keyword = request.args.get("query", None)
    context_dict = {
        "subtitle": f"Search Result for {keyword}",
        "keyword": keyword,
        "message": None if keyword else "Enter keywords back on the top page."
    }
    if keyword:
        return render_template("search.html", **context_dict)
    else:
        return render_template("index.html", **context_dict)
=======
    context_dict = {
        "message": "This is dummy message."
    }
    return render_template("index.html", **context_dict)
>>>>>>> 0dbd2e4502e80138fd46b37b21fca805df05b594


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
