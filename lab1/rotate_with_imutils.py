import cv2
import imutils

img = cv2.imread('media/image_lab1.png')
resized = imutils.resize(img, width=400)
rotated = imutils.rotate(resized, -45)
cv2.imshow("rotated imutils", rotated)
cv2.waitKey()
cv2.destroyAllWindows()
