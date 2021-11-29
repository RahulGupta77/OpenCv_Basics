import cv2

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial1/momo.png", 1)

# resizing image

# 1st method (Takes image and size in px as arguments)

newImg = cv2.resize(img, (400, 400))
cv2.imshow("resize", newImg)


# 2nd method (Takes image, (0,0), size of x [fx=(pixel size)], size of y [fy=(pixel size)] )

new_Img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
cv2.imshow("2ndMethod", new_Img)


cv2.waitKey(0)
cv2.destroyAllWindows()
