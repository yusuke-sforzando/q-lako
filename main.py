# !/usr/bin/env python3

from flask import flash, redirect, request, render_template, url_for

from __init__ import app


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    app.logger.info(f"search(): GET {request.full_path}.")
    keyword = request.args.get("query", None)
    if keyword:
        context_dict = {
            "subtitle": f"Search Result for {keyword}",
            "keyword": keyword,
        }
        return render_template("search.html", **context_dict)
    else:
        flash("Enter any keywords.", "warning")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
