import cv2

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Basics2/nami.png", -1)

copy = img[900:1400, 1000:1500]  # copying pixels in an array

img[100:600, 100:600] = copy  # pasting pixels in the image

cv2.imshow("Copy_Paste", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
