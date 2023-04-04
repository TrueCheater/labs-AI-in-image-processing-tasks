import cv2

face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
scaling_factor = 0.5

frame = cv2.imread('media/2_1.jpg')  # try 2_2.jpg, 2_3.jpg, 2_4.jpg
frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

print(f"Found faces: {len(face_rects)}")
for (x, y, w, h) in face_rects:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow('Watter White and Jesse Pinkman ', frame)
cv2.waitKey(0)
