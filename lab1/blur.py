import cv2
import imutils
import numpy as np

img = cv2.imread('media/image_lab1.png')
resized = imutils.resize(img, width=400)
blurred = cv2.GaussianBlur(resized, (11, 11), 0)
summing = np.hstack((resized, blurred))
cv2.imshow("cool image blurred", summing)
cv2.waitKey()
cv2.destroyAllWindows()
