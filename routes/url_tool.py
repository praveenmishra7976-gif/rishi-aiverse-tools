from flask import Blueprint, render_template, request
import urllib.parse

url_bp = Blueprint("url_tool", __name__)

@url_bp.route("/url-tool", methods=["GET", "POST"])
def url_tool():

    text = ""
    result = ""

    if request.method == "POST":

        text = request.form["text"]
        action = request.form["action"]

        if action == "encode":
            result = urllib.parse.quote(text)

        elif action == "decode":
            result = urllib.parse.unquote(text)

    return render_template(
        "tools/url_tool.html",
        text=text,
        result=result
    )
