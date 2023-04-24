from utils import face_encodings, nb_of_matches, face_rects
import cv2
import pickle

# toad the encodings + names dictionary
with open("encodings.pickle", "rb") as f:
    name_encodings_dict = pickle.load(f)

image = cv2.imread("examples/ag.jpg")
scaling_factor = 0.6
image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

# get the 128-d face embeddings for each face in the input image
encodings = face_encodings(image)

# the names of each face detected in the image
names = []

for encoding in encodings:
    counts = {}
    for (name, encodings) in name_encodings_dict.items():
        # compute the number of matches between the current encoding and the encodings
        # of the known faces and store the number of matches in the dictionary
        counts[name] = nb_of_matches(encodings, encoding)

    if all(count == 0 for count in counts.values()):
        name = "Unknown"
    else:
        name = max(counts, key=counts.get)

    names.append(name)

for rect, name in zip(face_rects(image), names):
    # get the bounding box for each face using the rect variable
    x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()

    # draw the bounding box of the face along with the name of the person
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
