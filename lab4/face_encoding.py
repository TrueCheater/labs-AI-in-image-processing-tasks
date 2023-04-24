from os import listdir, path
import pickle
import cv2
from utils import get_image_paths, face_encodings

root_dir = "dataset"
class_names = listdir(root_dir)

# get the paths to the images
image_paths = get_image_paths(root_dir, class_names)

# a dictionary to store the name of each person and the corresponding encodings
name_encodings_dict = {}

nb_current_image = 1  # initialize the number of images processed

for image_path in image_paths:
    print(f"Image processed {nb_current_image}/{len(image_paths)}")

    image = cv2.imread(image_path)
    encodings = face_encodings(image)  # get the face embeddings
    name = image_path.split(path.sep)[-2]  # get the name from the image path
    e = name_encodings_dict.get(name, [])  # get the encodings for the current name
    e.extend(encodings)  # update the list of encodings for the current name
    name_encodings_dict[name] = e
    nb_current_image += 1

# save the name encodings dictionary to disk
with open("encodings.pickle", "wb") as f:
    pickle.dump(name_encodings_dict, f)
