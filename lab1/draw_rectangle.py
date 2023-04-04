import cv2
import imutils

img = cv2.imread('media/image_lab1.png')
resized = imutils.resize(img, width=400)
cv2.rectangle(resized, (300, 150), (210, 70), (0, 0, 255), 2)
cv2.imshow("cool image rectangle", resized)
cv2.waitKey()
cv2.destroyAllWindows()
