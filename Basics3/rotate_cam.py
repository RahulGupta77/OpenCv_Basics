import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # there are 17 properties of cap.read(), look up the documentation for more
    ret, frame = cap.read()

    # cap.get(3) gives width of the frame captured/// by default it returns Float values
    width = int(cap.get(3))

    # cap.get(4) gives height of the frame captured/// by default it returns Float values
    height = int(cap.get(4))

    # gives an empty black screen to put our image onto
    image = np.zeros(frame.shape, np.uint8)

    # resizing the frame to fit in image window
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # shows image at top left corner and rotates it 180 degree
    image[: height // 2, : width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    # shows image at bottom left corner
    image[height // 2 :, : width // 2] = smaller_frame

    # shows image at top right corner and rotates it 180 degree
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    # shows image at bottom right corner
    image[height // 2 :, width // 2 :] = smaller_frame

    cv2.imshow("video", image)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
