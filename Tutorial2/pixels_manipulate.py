import cv2

import random

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial2/nami.png", 1)


for i in range(900, 1400):
    for j in range(img.shape[1]):
        img[i][j] = [
            random.randrange(255),
            random.randrange(255),
            random.randrange(255),
        ]
        # img[i][j] = [0, 128, 128]

cv2.imshow("changed", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
