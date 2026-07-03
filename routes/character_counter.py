from flask import Blueprint, render_template, request

character_counter_bp = Blueprint("character_counter", __name__)

@character_counter_bp.route("/character-counter", methods=["GET", "POST"])
def character_counter():

    text = ""
    characters = 0

    if request.method == "POST":
        text = request.form["text"]
        characters = len(text)

    return render_template(
        "tools/character_counter.html",
        text=text,
        characters=characters
    )
