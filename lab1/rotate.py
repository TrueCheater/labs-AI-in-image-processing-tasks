import cv2
import imutils

img = cv2.imread('media/image_lab1.png')
resized = imutils.resize(img, width=400)
h, w = resized.shape[0:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(resized, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey()
cv2.destroyAllWindows()
