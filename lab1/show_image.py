import cv2

img = cv2.imread('media/image_lab1.png')
cv2.imshow("cool image", img)
cv2.waitKey()
cv2.destroyAllWindows()
