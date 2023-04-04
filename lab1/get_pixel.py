import cv2

img = cv2.imread('media/image_lab1.png')
(blue, green, red) = img[350, 400]
print(f"{red = }, {green = }, {blue = }")
