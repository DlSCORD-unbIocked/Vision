import cv2
import numpy as np
import face_recognition

image = face_recognition.load_image_file("test.png")
face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
print(face_landmarks_list)
