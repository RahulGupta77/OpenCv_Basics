import cv2 as cv

img = cv.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial2/nami.png", -1)

copy = img[900:1400, 1000:1500]  # copying pixels in an array

img[100:600, 100:600] = copy  # pasting pixels in the image

cv.imshow("Copy_Paste", img)

cv.waitKey(0)
cv.destroyAllWindows
