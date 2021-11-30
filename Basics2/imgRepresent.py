import cv2

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Basics2/nami.png", 1)

# # printing type of image which basically is numpy ndArray
# print(type(img))

# image is represented as 3-d arrays rows, coloumns, channels

print(img[500, 1000:1500])

# cv2.waitKey(0)
# cv2.destroyAllWindows()
