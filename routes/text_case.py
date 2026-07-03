from flask import Blueprint, render_template, request

text_case_bp = Blueprint("text_case", __name__)

@text_case_bp.route("/text-case", methods=["GET", "POST"])
def text_case():

    text = ""
    result = ""

    if request.method == "POST":

        text = request.form["text"]
        action = request.form["action"]

        if action == "upper":
            result = text.upper()

        elif action == "lower":
            result = text.lower()

        elif action == "title":
            result = text.title()

        elif action == "capitalize":
            result = text.capitalize()

    return render_template(
        "tools/text_case.html",
        text=text,
        result=result
    )
