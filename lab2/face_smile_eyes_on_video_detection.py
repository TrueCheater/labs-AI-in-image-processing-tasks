import cv2

face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_eye.xml')

cap = cv2.VideoCapture('media/5.mp4')

scaling_factor = 0.5

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(gray_filter, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        roi_gray = gray_filter[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        smile = smile_cascade.detectMultiScale(roi_gray)
        eye = eye_cascade.detectMultiScale(roi_gray)

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)

        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)

    cv2.imshow('Mia', frame)
    if cv2.waitKey(2) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
