import cv2

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial1/momo.png", 1)

# rotating image (takes 2 args image_var name, angle that you want to rotate)
# (Read documentation for more angle
# second argument can consist of
# cv2.cv2.ROTATE_90_COUNTERCLOCKWISE
# cv2.cv2.ROTATE_90_CLOCKWISE
# cv2.cv2.ROTATE_180

rotImg = cv2.rotate(img, cv2.cv2.ROTATE_180)


cv2.imshow("Rotate", rotImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
