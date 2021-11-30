# displaying circle in the video frame

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # cv2.circle(src img, centre co-ordinates, radius , color, thickness)

    img = cv2.circle(frame, (width // 2, height // 2), 200, (255, 0, 0), 3)

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
