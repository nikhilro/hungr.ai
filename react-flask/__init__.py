import pkg_resources

from os import environ, path
from flask import Flask, render_template, send_from_directory, Response
from flask_webpack import Webpack
from helper import gen
from camera_pi import Camera


__version__ = pkg_resources.require("demo")[0].version
here = path.abspath(path.dirname(__file__))

app = Flask(__name__)
debug = "DEBUG" in environ

webpack = Webpack()
app.config["WEBPACK_MANIFEST_PATH"] = path.join(here, "manifest.json")
webpack.init_app(app)


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/assets/<path:filename>")
def send_asset(filename):
    return send_from_directory(path.join(here, "public"), filename)

if __name__ == "__main__":
    app.debug = debug
    app.run(extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
