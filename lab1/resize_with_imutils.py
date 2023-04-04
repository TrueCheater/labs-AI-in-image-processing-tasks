import cv2
import imutils

img = cv2.imread('media/image_lab1.png')
cv2.imshow("cool image", img)
resized = imutils.resize(img, width=300)
cv2.imshow("resized imutils", resized)
cv2.waitKey()
cv2.destroyAllWindows()
