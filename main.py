# !/usr/bin/env python3

from flask import render_template

from __init__ import app


@app.route("/", methods=["GET"])
def index():
    app.logger.info("index(): GET /")
    context_dict = {
        "message": "This is dummy message."
    }
    return render_template("index.html", **context_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
