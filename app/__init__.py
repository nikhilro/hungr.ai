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

# #!/usr/bin/env python
# """
# Creates an HTTP server with basic auth and websocket communication.
# """
# import argparse
# import base64
# import os
# import webbrowser
# from os import path
#
# try:
#     import cStringIO as io
# except ImportError:
#     import io
#
# from tornado_cors import CorsMixin
# import tornado.web
# import tornado.websocket
# from tornado.ioloop import PeriodicCallback
#
# # Hashed password for comparison and a cookie for login cache
# ROOT = os.path.normpath(os.path.dirname(__file__))
# here = path.abspath(path.dirname(__file__))
# WEBCAM = True
# port = 8000
#
#
# class IndexHandler(CorsMixin, tornado.web.RequestHandler):
#
#     def get(self):
#         template_path = path.join(here, "manifest.json")
#         self.ctx.eval_string('React.renderToString(React.createElement(Components.Hello));')
#         self.write(self.ctx.get())
#         self.ctx.pop()
#         self.render("templates/index.html", port=port)
#
#
# class WebSocket(tornado.websocket.WebSocketHandler):
#
#     def on_message(self, message):
#         """Evaluates the function pointed to by json-rpc."""
#
#         # Start an infinite loop when this is called
#         if message == "read_camera":
#             self.camera_loop = PeriodicCallback(self.loop, 10)
#             self.camera_loop.start()
#
#         # Extensibility for other methods
#         else:
#             print("Unsupported function: " + message)
#
#     def loop(self):
#         """Sends camera images in an infinite loop."""
#         sio = io.StringIO()
#
#         if WEBCAM:
#             _, frame = camera.read()
#             try:
#                 img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#                 img.save(sio, "JPEG")
#             except Exception:
#                 print('empty file')
#         else:
#             camera.capture(sio, "jpeg", use_video_port=True)
#
#         try:
#             self.write_message(base64.b64encode(sio.getvalue()))
#         except tornado.websocket.WebSocketClosedError:
#             self.camera_loop.stop()
#
#
# parser = argparse.ArgumentParser(description="Starts a webserver that "
#                                  "connects to a webcam.")
# parser.add_argument("--port", type=int, default=8000, help="The "
#                     "port on which to serve the website.")
# parser.add_argument("--resolution", type=str, default="low", help="The "
#                     "video resolution. Can be high, medium, or low.")
# parser.add_argument("--require-login", action="store_true", help="Require "
#                     "a password to log in to webserver.")
# parser.add_argument("--use-usb", action="store_true", help="Use a USB "
#                     "webcam instead of the standard Pi camera.")
# parser.add_argument("--usb-id", type=int, default=0, help="The "
#                      "usb camera number to display")
# args = parser.parse_args()
#
# if WEBCAM:
#     import cv2
#     from PIL import Image
#     camera = cv2.VideoCapture(args.usb_id)
# else:
#     import picamera
#     camera = picamera.PiCamera()
#     camera.start_preview()
#
# resolutions = {"high": (1280, 720), "medium": (640, 480), "low": (320, 240)}
# if args.resolution in resolutions:
#     if WEBCAM:
#         w, h = resolutions[args.resolution]
#         camera.set(3, w)
#         camera.set(4, h)
#     else:
#         camera.resolution = resolutions[args.resolution]
# else:
#     raise Exception("%s not in resolution options." % args.resolution)
#
# handlers = [(r"/", IndexHandler),
#             (r"/websocket", WebSocket),
#             (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': ROOT})]
# application = tornado.web.Application(handlers)
# application.listen(port)
#
# webbrowser.open("http://localhost:%d/" % port, new=2)
#
# tornado.ioloop.IOLoop.instance().start()
