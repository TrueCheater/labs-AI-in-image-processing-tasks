import cv2
import numpy as np

img = np.zeros((200, 200, 3), np.uint8)
points = np.array([[0, 0], [100, 50], [50, 100], [0, 0]])
cv2.polylines(img, np.int32([points]), 1, (255, 255, 255))
cv2.imshow("cool image lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
