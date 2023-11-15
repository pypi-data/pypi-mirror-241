import time
import cv2

from .model import load_model
from ..error import ToolsTimeoutError, ToolsFileError


def face_detection(input_path: str, model_name: str, proportion: float, timeout: int) -> bool:
    model_path = load_model(model_name)
    face_detector = cv2.CascadeClassifier(model_path)

    video = None
    total_frames = 0
    total_faces = 0
    try:
        print('face detection start...')
        video = cv2.VideoCapture(input_path)
        start_time = time.time()

        while video.isOpened():
            if (timeout is not None) and (time.time() - start_time > timeout):
                raise ToolsTimeoutError("face detection timeout")

            ret, frame = video.read()  # 逐帧读取视频流(ret-是否读取到帧, frame-是读取的帧内容)
            if not ret:
                break
            total_frames += 1

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(frame)

            if len(faces) > 0:
                total_faces += 1
        else:
            raise ToolsFileError("unexpected file closure")

        return float(total_faces / total_frames) >= proportion
    finally:
        if video:
            video.release()
        print(f'face detection finished: {total_frames=} {total_faces=}')
