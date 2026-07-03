from flask import Blueprint, render_template, request
from datetime import datetime

age_bp = Blueprint("age", __name__)

@age_bp.route("/age", methods=["GET", "POST"])
def age():

    age = None

    if request.method == "POST":

        dob = request.form["dob"]

        birth = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()

        age = today.year - birth.year - (
            (today.month, today.day) < (birth.month, birth.day)
        )

    return render_template("tools/age.html", age=age)
