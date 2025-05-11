# Face Verification

Dự án nhận diện và xác thực khuôn mặt sử dụng Python, OpenCV và dlib/face_recognition. Hệ thống có khả năng nhận diện người dùng từ hình ảnh hoặc video, và xác thực xem khuôn mặt có thuộc về người đã đăng ký trước đó không.

## 📦 Tính năng chính

- Phát hiện và nhận diện khuôn mặt từ ảnh và video.
- Mã hóa khuôn mặt và lưu dưới dạng file `pickle`.
- So sánh embedding khuôn mặt để xác minh danh tính.
- Hỗ trợ xác minh thời gian thực từ webcam hoặc file video.
- Quản lý dataset người dùng dễ dàng.

## 🛠 Công nghệ sử dụng

- Python 3.8+
- [face_recognition](https://github.com/ageitgey/face_recognition)
- OpenCV
- dlib
- NumPy
- Pickle

## 📁 Cấu trúc thư mục

```bash
Face_verification/
├── dataset/              # Thư mục chứa ảnh gốc của người dùng
├── encoding.pickle       # File chứa các vector khuôn mặt đã mã hóa
├── test_images/          # Thư mục ảnh để test xác thực
├── test_video/           # Thư mục chứa video để test
├── main/                 # Thư mục chứa các script chính để chạy hệ thống
├── .gitignore
├── README.md
