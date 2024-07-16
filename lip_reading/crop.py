import cv2
import numpy as np
import face_recognition
from cameras import Camera


class LipCropper:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.cropped_image = None

    def load_image(self):
        self.image = face_recognition.load_image_file(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"Image {self.image_path} not found.")

    def find_face_landmarks(self):
        face_locations = face_recognition.face_locations(self.image)
        face_landmarks_list = face_recognition.face_landmarks(self.image)
        if not face_landmarks_list:
            raise ValueError("No faces or landmarks found in the image.")
        return face_landmarks_list[0]

    def crop_mouth(self):
        self.load_image()
        landmarks = self.find_face_landmarks()
        top_lip_points = landmarks['top_lip']
        bottom_lip_points = landmarks['bottom_lip']
        mouth_points = top_lip_points + bottom_lip_points

        x_min = min(point[0] for point in mouth_points)
        x_max = max(point[0] for point in mouth_points)
        y_min = min(point[1] for point in mouth_points)
        y_max = max(point[1] for point in mouth_points)

        image_cv = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        self.cropped_image = image_cv[y_min:y_max, x_min:x_max]

    def show_cropped_mouth(self):
        if self.cropped_image is not None:
            cv2.imshow("Mouth Crop", self.cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No cropped image to display. Please run crop_mouth() first.")
