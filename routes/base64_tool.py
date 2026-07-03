from flask import Blueprint, render_template, request
import base64

base64_bp = Blueprint("base64", __name__)

@base64_bp.route("/base64", methods=["GET", "POST"])
def base64_tool():

    text = ""
    result = ""

    if request.method == "POST":

        text = request.form["text"]
        action = request.form["action"]

        try:
            if action == "encode":
                result = base64.b64encode(text.encode()).decode()

            elif action == "decode":
                result = base64.b64decode(text.encode()).decode()

        except Exception:
            result = "Invalid Base64 Text"

    return render_template(
        "tools/base64_tool.html",
        text=text,
        result=result
    )
