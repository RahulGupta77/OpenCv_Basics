# displaying text in the video frame


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # for displaying text we need to specify the font first
    # we need to specify following things:
    #         --> img src
    #         --> text to be displayed
    #         --> position of text
    #         --> font
    #         --> scale (how large he text should be)
    #         --> color
    #         --> thickness
    #         --> linetype (putting "cv2.LINE_AA" is recommended)

    font = cv2.FONT_HERSHEY_SIMPLEX

    img = cv2.putText(
        frame,
        "Learning OpenCV",
        (100, height - 50),
        font,
        2,
        (0, 0, 255),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
