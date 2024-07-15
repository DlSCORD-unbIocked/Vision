import cv2
import numpy as np
import time


class Camera:
    def __init__(self, camera_id, api_preference=cv2.CAP_ANY):
        self.cap = cv2.VideoCapture(camera_id, api_preference)
        # Can be whatever values work to get 20+ fps
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1919)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()

    def __del__(self):
        self.release()


if __name__ == "__main__":
    # Change dshow or 0 for whatever works for your camera
    camera = Camera(0, cv2.CAP_DSHOW)

    while True:
        frame = camera.get_frame()
        # if frame:
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
