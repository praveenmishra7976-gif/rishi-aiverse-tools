from flask import Blueprint, render_template, request
import qrcode

qr_bp = Blueprint("qr", __name__)

@qr_bp.route("/qr", methods=["GET", "POST"])
def qr():

    qr = None

    if request.method == "POST":
        text = request.form["text"]

        img = qrcode.make(text)
        img.save("static/qrcode.png")

        qr = "qrcode.png"

    return render_template("tools/qr.html", qr=qr)
