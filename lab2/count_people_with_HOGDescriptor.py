import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

scaling_factor = 0.25
frame = cv2.imread('media/4.jpg')
frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
people_rects = hog.detectMultiScale(frame, winStride=(8, 8), padding=(30, 30), scale=1.06)

for (x, y, w, h) in people_rects[0]:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Harry, Ron and Hermione', frame)
cv2.waitKey(0)
