import cv2

img = cv2.imread('media/image_lab1.png')
cv2.line(img, (0, 0), (600, 499), (255, 0, 0), 3)
cv2.imshow("cool image line", img)
cv2.waitKey()
cv2.destroyAllWindows()
