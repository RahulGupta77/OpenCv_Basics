# displaying line in the video frame


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # cv2.line(src img, starting co-ordinate, ending co-ordinate, color, thickness)
    # Note----> OpenCV has different co-ordinate system.

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)
    # img = cv2.line(frame, (width, 0), (0, height), (255, 0, 0), 5)
    # img = cv2.line(frame, (0, height // 2), (width, height // 2), (255, 0, 0), 5)
    # img = cv2.line(frame, (width // 2, 0), (width // 2, height), (255, 0, 0), 5)

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
