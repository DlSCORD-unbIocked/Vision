import cv2
from cameras import Camera

capture = Camera(0, 2880, 1800, cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (2880, 1800))

while True:
    ret, frame = capture.read()
    if not ret:
        print("Error reading frame")
        break

    out.write(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()