import cv2

img = cv2.imread('media/image_lab1.png')
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'take the shot', (340, 100), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imshow("cool image with new text", img)
cv2.waitKey()
cv2.destroyAllWindows()
