import cv2
import numpy

fase_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

cap = cv2.VideoCapture('media/6.mp4')
scaling_factor = 0.3

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    face_rects = fase_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    people_rects, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    people_rects = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in people_rects])

    for (xa, ya, xb, yb) in people_rects:
        cv2.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 255), 1)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('London street', frame)
    if cv2.waitKey(2) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
