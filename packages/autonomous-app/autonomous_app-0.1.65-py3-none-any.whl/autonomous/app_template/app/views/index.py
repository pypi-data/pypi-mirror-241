# Built-In Modules

# external Modules
from flask import Blueprint, render_template, request, session

from autonomous import log
from autonomous.auth import auth_required

index_page = Blueprint("index", __name__)


@index_page.route("/", methods=("GET",))
def index():
    return render_template("index.html")


@index_page.route(
    "/protected",
    methods=(
        "GET",
        "POST",
    ),
)
@auth_required
def protected():
    context = {"user": session.get("user")}
    return render_template("index.html", **context)
