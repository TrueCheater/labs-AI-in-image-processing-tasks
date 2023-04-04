import cv2

face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
frame = cv2.imread('media/1.png')
face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

print(f"Found faces: {len(face_rects)}")
for (x, y, w, h) in face_rects:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow('Gus', frame)
cv2.waitKey(0)
