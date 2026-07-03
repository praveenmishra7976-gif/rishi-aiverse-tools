from flask import Blueprint, render_template, request
import random
import string

password_bp = Blueprint("password", __name__)

@password_bp.route("/password", methods=["GET", "POST"])
def password():

    result = ""

    if request.method == "POST":
        length = int(request.form["length"])

        characters = string.ascii_letters + string.digits + "!@#$%^&*()"

        result = "".join(random.choice(characters) for _ in range(length))

    return render_template("tools/password.html", password=result)
