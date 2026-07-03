from flask import Blueprint, render_template, request

unit_bp = Blueprint("unit", __name__)

@unit_bp.route("/unit-converter", methods=["GET", "POST"])
def unit_converter():

    result = None

    if request.method == "POST":

        value = float(request.form["value"])
        conversion = request.form["conversion"]

        if conversion == "km_to_m":
            result = value * 1000

        elif conversion == "m_to_km":
            result = value / 1000

        elif conversion == "kg_to_g":
            result = value * 1000

        elif conversion == "g_to_kg":
            result = value / 1000

        elif conversion == "c_to_f":
            result = (value * 9/5) + 32

        elif conversion == "f_to_c":
            result = (value - 32) * 5/9

    return render_template(
        "tools/unit_converter.html",
        result=result
    )
