import cv2

img = cv2.imread('media/image_lab1.png')
resized = cv2.resize(img, (400, 200))
cv2.imshow("cool image", resized)
cv2.waitKey()
cv2.destroyAllWindows()
