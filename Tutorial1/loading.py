import cv2

# loading image takes 2 commands--> 1st arg as Path of the image, 2nd arg is type that you want to import in.
# for 2nd type arg we can load in:
#           1. -1 or cv2.IMREAD_COLOR : Loads a color image. Any transperacy of image will be neglected. It is default FLag.
#           2. 0 or cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode.
#           3. 1 or cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel.

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial1/momo.png", -1)


# rotating Image
rotImg = cv2.rotate(img, cv2.cv2.ROTATE_180)
cv2.imshow("Rotate image", rotImg)
# cv2.imshow("Momo", img)
cv2.imwrite("new_momo.png", rotImg)
cv2.waitKey(0)
cv2.destroyAllWindows
