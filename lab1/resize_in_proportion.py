import cv2

img = cv2.imread('media/image_lab1.png')
cv2.imshow("cool image", img)
h, w = img.shape[0:2]
h_new = 250
ratio = w / h
w_new = int(h_new * ratio)
resized = cv2.resize(img, (w_new, h_new))
cv2.imshow("resized", resized)
cv2.waitKey()
cv2.destroyAllWindows()
