import cv2
import os
from deepface import DeepFace


def create_dirs(base_dir, sub_dirs):
    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)


input_dir = "input_images"
output_dir = "output"
create_dirs(output_dir, ["original_with_faces", "cropped_faces"])


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def process_image(image_path, output_dir):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    cropped_faces = []
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (224, 224))  # Приведение к общему размеру
        cropped_faces.append(face_resized)

        try:
            analysis = DeepFace.analyze(face_resized, actions=['emotion'], enforce_detection=False)
            emotion = analysis['dominant_emotion']
        except Exception as e:
            emotion = "Unknown"

        face_output_path = os.path.join(output_dir, "cropped_faces", f"{os.path.basename(image_path)}_face_{i}_{emotion}.jpg")
        cv2.imwrite(face_output_path, face_resized)

        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    original_output_path = os.path.join(output_dir, "original_with_faces", os.path.basename(image_path))
    cv2.imwrite(original_output_path, image)

for file_name in os.listdir(input_dir):
    if file_name.lower().endswith(('png', 'jpg', 'jpeg')):
        process_image(os.path.join(input_dir, file_name), output_dir)
