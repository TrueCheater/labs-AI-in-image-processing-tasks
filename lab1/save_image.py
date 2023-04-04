import cv2

img = cv2.imread('media/image_lab1.png', 0)
cv2.imwrite('image_lab1_gray.png', img)
img = cv2.imread('media/image_lab1_gray.png')
cv2.imshow("cool image in gray", img)
cv2.waitKey()
cv2.destroyAllWindows()
