import cv2

img = cv2.imread('media/image_lab1.png')
cv2.imshow("cool image", img)
roi = img[20:200, 40:250]
cv2.imshow("roi", roi)
cv2.waitKey()
cv2.destroyAllWindows()
