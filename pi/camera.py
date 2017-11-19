import cv2
import base64
import time
# from base_camera import BaseCamera
from PIL import Image

try:
    import cStringIO as io
except ImportError:
    import io


class Camera():
    @staticmethod
    def get_frame(socketio):
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FPS, 30)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        sio = io.BytesIO()

        while True:
            time.sleep(0.1)
            _, frame = camera.read()
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.save(sio, format="JPEG")
            # sio.seek(0)

            # encode as jpg and return
            # return cv2.imencode('.jpg', img)[1].tobytes()
            socketio.emit('videoStart', {
                "data": base64.b64encode(sio.getvalue())
            })
