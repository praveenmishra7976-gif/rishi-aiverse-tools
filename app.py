from flask import Flask, render_template

from routes.qr import qr_bp
from routes.password import password_bp
from routes.age import age_bp
from routes.bmi import bmi_bp
from routes.word_counter import word_counter_bp
from routes.character_counter import character_counter_bp
from routes.text_case import text_case_bp
from routes.base64_tool import base64_bp
from routes.url_tool import url_bp
from routes.unit_converter import unit_bp

app = Flask(__name__)

app.register_blueprint(qr_bp)
app.register_blueprint(password_bp)
app.register_blueprint(age_bp)
app.register_blueprint(bmi_bp)
app.register_blueprint(word_counter_bp)
app.register_blueprint(character_counter_bp)
app.register_blueprint(text_case_bp)
app.register_blueprint(base64_bp)
app.register_blueprint(url_bp)
app.register_blueprint(unit_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
