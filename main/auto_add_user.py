# ==== File: auto_add_user.py ====
import face_recognition
import pickle
import cv2
import os

ENCODINGS_PATH = "encoding.pickle"
NEW_USER_NAME = input("Enter the name for new user: ")
SAVE_IMAGE_DIR = os.path.join("dataset", NEW_USER_NAME)

os.makedirs(SAVE_IMAGE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

while count < 20:  # Save 20 images
    ret, frame = cap.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")

    for (top, right, bottom, left) in boxes:
        face = frame[top:bottom, left:right]
        face = cv2.resize(face, (150, 150))
        img_path = os.path.join(SAVE_IMAGE_DIR, f"{NEW_USER_NAME}_{count}.jpg")
        cv2.imwrite(img_path, face)
        count += 1
        print(f"[INFO] Saved {img_path}")

    cv2.imshow("Capture Faces", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("[INFO] Capture done. Now re-run encode_faces.py!")

# import cv2
# import os
# import time

# # Khởi tạo camera
# cam = cv2.VideoCapture(0)
# cam.set(3, 640)
# cam.set(4, 480)

# # Load bộ phân loại
# face_detector_frontal = cv2.CascadeClassifier('/Users/macbook/Desktop/Mobile_Netv1/haarcascade_frontalface_default.xml')
# face_detector_profile = cv2.CascadeClassifier('/Users/macbook/Desktop/Mobile_Netv1/haarcascade_profileface.xml')

# # Nhập ID
# face_id = input('\nNhập ID khuôn mặt: ')
# print('\n[INFO] Khởi tạo camera...')

# # Tạo thư mục dataset
# dataset_dir = f"/Users/macbook/Desktop/Mobile_Netv1/dataset/{face_id}"
# os.makedirs(dataset_dir, exist_ok=True)

# # Các trạng thái cần thu thập
# modes = ["frontal", "right", "left"]
# mode_text = {
#     "frontal": "Nhìn thẳng vào camera",
#     "right": "Nghiêng mặt sang phải",
#     "left": "Nghiêng mặt sang trái"
# }

# total_images_per_mode = 60
# delay_between_shots = 0.01  # 0.2s

# for mode in modes:
#     print(f"\n[HƯỚNG DẪN] Vui lòng {mode_text[mode]}...")
#     time.sleep(3)

#     count = 0
#     while count < total_images_per_mode:
#         ret, frame = cam.read()
#         if not ret:
#             break

#         frame = cv2.flip(frame, 1)  # Lật hình cho giống gương
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         faces = []
#         if mode == "frontal":
#             faces = face_detector_frontal.detectMultiScale(gray, 1.1, 5)
#         elif mode == "right":
#             flipped_gray = cv2.flip(gray, 1)
#             faces_raw = face_detector_profile.detectMultiScale(flipped_gray, 1.1, 5)
#             for (x, y, w, h) in faces_raw:
#                 x = gray.shape[1] - x - w
#                 faces.append((x, y, w, h))
#         elif mode == "left":
#             faces = face_detector_profile.detectMultiScale(gray, 1.1, 5)

#         for (x, y, w, h) in faces:
#             face_img = rgb[y:y+h, x:x+w]
#             if face_img.size > 0:
#                 # Resize về kích thước chuẩn 224x224
#                 face_resized = cv2.resize(face_img, (224, 224))
#                 filename = f"{dataset_dir}/user.{face_id}.{mode}.{count}.jpg"
#                 cv2.imwrite(filename, cv2.cvtColor(face_resized, cv2.COLOR_RGB2BGR))  # Lưu lại theo định dạng BGR
#                 count += 1
#                 # Vẽ hộp quanh mặt
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         cv2.putText(frame, f"{mode_text[mode]} - Count: {count}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
#         cv2.imshow('Face Capture', frame)

#         key = cv2.waitKey(1)
#         if key == 27:  # ESC
#             break

#         time.sleep(delay_between_shots)

# print("\n[INFO] Đã hoàn tất thu thập 180 ảnh (60 chính diện, 60 phải, 60 trái)!")
# cam.release()
# cv2.destroyAllWindows()
