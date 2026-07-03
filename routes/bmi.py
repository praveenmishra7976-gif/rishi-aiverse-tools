from flask import Blueprint, render_template, request

bmi_bp = Blueprint("bmi", __name__)

@bmi_bp.route("/bmi", methods=["GET", "POST"])
def bmi():

    bmi = None
    status = ""

    if request.method == "POST":

        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal Weight"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

    return render_template(
        "tools/bmi.html",
        bmi=bmi,
        status=status
    )
