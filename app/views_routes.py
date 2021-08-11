from app import app

from flask import request, render_template
from app.classify import get_class_ml

@app.route("/")
def index():

    """
    This route will render a template.
    If a query string comes into the URL, it will return a parsed
    dictionary of the query string keys & values, using request.args
    """

    args = None

    if request.args:

        args = request.args
        return render_template("public/index.html", args=args)

    return render_template("public/index.html", args=args)


@app.route("/task", methods=["POST"])
def get_class():

    data = request.get_data()
    return get_class_ml(str(data))
