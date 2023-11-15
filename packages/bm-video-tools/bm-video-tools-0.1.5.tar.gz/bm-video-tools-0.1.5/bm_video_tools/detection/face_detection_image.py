import cv2

from .model import load_model


def face_detection(input_path: str, model_name: str, ) -> bool:
    model_path = load_model(model_name)
    face_detector = cv2.CascadeClassifier(model_path)
    img = cv2.imread(input_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_detector.detectMultiScale(img)
    return len(faces) > 0
