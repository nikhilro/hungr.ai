import pkg_resources

from datetime import timedelta
from os import environ, path
from flask import Flask, render_template, send_from_directory, request, current_app, make_response
from flask_webpack import Webpack
from flask_cors import CORS
from functools import update_wrapper
# from flask_socketio import SocketIO
# from opencv.multipleBalls
# from camera import Camera


__version__ = pkg_resources.require("hungr.ai")[0].version
here = path.abspath(path.dirname(__file__))

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
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

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


# App Routes
@app.route("/")
@crossdomain(origin='*')
def index():
    return render_template("index.html")


@app.route("/img", methods=['POST'])
def set_image():
    data = request.get_json()['data']


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# <!-- <img src="{{ url_for('video_feed') }}"> -->

@app.route("/assets/<path:filename>")
def send_asset(filename):
    return send_from_directory(path.join(here, "public"), filename)


# Socket Routes
# @socketio.on('readCamera')
# def read_camera():
#     print('Reading camera...')
    # Camera().get_frame(socketio)


if __name__ == "__main__":
    app.debug = debug
    app.run(extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
    # socketio.run(app, extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
