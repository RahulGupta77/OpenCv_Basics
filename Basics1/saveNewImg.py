import cv2

img = cv2.imread("/Volumes/T5/OpenCV/TWT_openCV_tutorial/Tutorial1/momo.png", 1)

newImg = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# saving new image. It takes two arguments ("Name_of_the_file", image to be saved)

cv2.imwrite("new_Img.png", newImg)
