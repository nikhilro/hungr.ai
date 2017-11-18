import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def get_frame():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            _, img = camera.read()

            # encode as jpg and return
            return cv2.imencode('.jpg', img)[1].tobytes()
