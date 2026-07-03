from flask import Blueprint, render_template, request

word_counter_bp = Blueprint("word_counter", __name__)

@word_counter_bp.route("/word-counter", methods=["GET", "POST"])
def word_counter():

    text = ""
    words = 0
    characters = 0

    if request.method == "POST":
        text = request.form["text"]
        words = len(text.split())
        characters = len(text)

    return render_template(
        "tools/word_counter.html",
        text=text,
        words=words,
        characters=characters
    )
