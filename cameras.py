import cv2
import numpy as np
import time


class Camera:
    def __init__(self, camera_id, width, height, api_preference=cv2.CAP_ANY):
        self.cap = cv2.VideoCapture(camera_id, api_preference)
        # Can be whatever values work to get 20+ fps
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def read(self):
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        self.cap.release()

    def __del__(self):
        self.release()


if __name__ == "__main__":
    # Change dshow or 0 for whatever works for your camera
    camera = Camera(0, 1919, 1080, cv2.CAP_DSHOW)

    while True:
        ret, frame = camera.read()
        # if frame:
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
