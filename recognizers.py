from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizerResult
from mediapipe.tasks.python.vision.hand_landmarker import HandLandmarkerResult

def count_fingers(landmark_result: HandLandmarkerResult) -> int:
    return 0

def recognize_victory(gesture_result: GestureRecognizerResult) -> bool:
    return False

def recognize_thumbs_up(gesture_result: GestureRecognizerResult) -> bool:
    return False