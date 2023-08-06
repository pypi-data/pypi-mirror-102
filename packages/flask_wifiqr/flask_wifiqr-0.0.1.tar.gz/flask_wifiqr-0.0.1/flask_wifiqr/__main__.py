# coding=utf-8
import os

from flask import Flask, render_template, send_file
from flask_qrcode import QRcode

app = Flask(
    import_name=__name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates')
)

qrcode = QRcode(app)


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    ssid = os.getenv('WIFI_SSID', 'unknown')
    password = os.getenv('WIFI_PASSWORD', 'notset')

    return send_file(
        qrcode(f"WIFI:S:{ssid};T:WPA;P:{password};;", mode="raw", border=5, box_size=20),
        mimetype="image/png"
    )


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


def main():
    app.run(
        host="0.0.0.0",
        debug=int(os.getenv('DEBUG', 0))
    )


if __name__ == '__main__':
    main()




