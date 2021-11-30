# displaying rectangle in the video frame


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # cv2.rectangle(src img, top-left corner co-ordinate, bottom-right corner co-ordinate, color, thickness)

    img = cv2.rectangle(
        frame,
        (width // 2 - 100, height // 2 - 50),
        (width // 2 + 100, height // 2 + 50),
        (0, 0, 255),
        3,
    )

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
