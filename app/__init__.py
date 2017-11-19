import pkg_resources

from os import environ, path
from flask import Flask, render_template, send_from_directory
from flask_webpack import Webpack
from flask_socketio import SocketIO
from camera import Camera


__version__ = pkg_resources.require("hungr.ai")[0].version
here = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
debug = "DEBUG" in environ

webpack = Webpack()
app.config["WEBPACK_MANIFEST_PATH"] = path.join(here, "manifest.json")
webpack.init_app(app)


# def gen(camera):
#     """Video streaming generator function."""
#     while True:
#         frame = camera.get_frame()
#         socketio.emit('videoStart', {
#             "data": b'--frame\r\n'
#                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
#         })


# App Routes
@app.route("/")
def index():
    return render_template("index.html")


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# <!-- <img src="{{ url_for('video_feed') }}"> -->


@app.route("/assets/<path:filename>")
def send_asset(filename):
    return send_from_directory(path.join(here, "public"), filename)


# Socket Routes
@socketio.on('readCamera')
def read_camera():
    print('Reading camera...')
    # Camera().get_frame(socketio)


if __name__ == "__main__":
    app.debug = debug
    socketio.run(app, extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
