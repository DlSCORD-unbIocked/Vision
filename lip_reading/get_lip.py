import cv2
import face_recognition
from cameras import Camera

def draw_points(image, points, color=(0, 255, 0), thickness=2):
    for point in points:
        cv2.circle(image, point, 1, color, thickness)

capture = Camera(0, 2880, 1800, cv2.CAP_DSHOW)
while True:
    ret, frame = capture.read()
    if not ret:
        print("Error reading frame")
        break
    face_landmarks_list = face_recognition.face_landmarks(frame)
    if not face_landmarks_list:
        continue
    image_cv = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    top_lip = face_landmarks_list[0]['top_lip']
    bottom_lip = face_landmarks_list[0]['bottom_lip']

    draw_points(image_cv, top_lip)

    draw_points(image_cv, bottom_lip)

    cv2.imshow("frame", image_cv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break