import face_recognition
import pickle
import os

DATASET_DIR = "/Users/macbook/Desktop/Face_Verification/dataset"
ENCODINGS_PATH = "encoding.pickle"

encodings = []
names = []

for person_name in os.listdir(DATASET_DIR):
    person_folder = os.path.join(DATASET_DIR, person_name)
    # print(f"[INFO] Processing {person_name}...")
    # print(f"[INFO] Person folder: {person_folder}")
    if not os.path.isdir(person_folder):
        continue

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        image = face_recognition.load_image_file(img_path)

        # "hog"	Histogram of Oriented Gradients	Nhanh, nhẹ, chạy được trên CPU, nhưng độ chính xác vừa phải.
        # "cnn"	Convolutional Neural Network	Chính xác hơn nhiều, nhưng chậm hơn, và cần GPU để chạy nhanh
        boxes = face_recognition.face_locations(image, model="hog")
        encodes = face_recognition.face_encodings(image, boxes)

        for encode in encodes:
            encodings.append(encode)
            names.append(person_name)

print(f"[INFO] Encoded {len(encodings)} faces.")

# Save encodings
with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump({"encodings": encodings, "names": names}, f)

print("[INFO] Saved encodings to encoding.pickle")