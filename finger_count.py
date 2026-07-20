    
import cv2
import math
import time
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ==========================================
# MediaPipe Tasks HandLandmarker Setup
# ==========================================

MODEL_PATH = "hand_landmarker.task"

base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

hand_landmarker = vision.HandLandmarker.create_from_options(options)


# ==========================================
# Hand Landmark Connections
# ==========================================

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),          # Thumb
    (0,5),(5,6),(6,7),(7,8),          # Index
    (5,9),(9,10),(10,11),(11,12),     # Middle
    (9,13),(13,14),(14,15),(15,16),   # Ring
    (13,17),(17,18),(18,19),(19,20),  # Pinky
    (0,17)
]

# ==========================================
# Landmark Indexes
# ==========================================

finger_tips = [8, 12, 16, 20]
finger_pips = [6, 10, 14, 18]

thumb_tip = 4
thumb_mcp = 2

wrist = 0

# ==========================================
# Utility Functions
# ==========================================

def calculate_distance(point1, point2):
    """
    Euclidean distance between two MediaPipe landmarks
    """

    return math.sqrt(
        (point1.x - point2.x) ** 2 +
        (point1.y - point2.y) ** 2 +
        (point1.z - point2.z) ** 2
    )

def draw_hand(frame, landmarks):
    """
    Draw hand landmarks using OpenCV.
    This replaces mp.solutions.drawing_utils.
    """

    height, width = frame.shape[:2]

    # Draw bones
    for start, end in HAND_CONNECTIONS:

        x1 = int(landmarks[start].x * width)
        y1 = int(landmarks[start].y * height)

        x2 = int(landmarks[end].x * width)
        y2 = int(landmarks[end].y * height)

        cv2.line(
            frame,
            (x1, y1),
            (x2, y2),
            (255, 0, 0),
            2
        )

    # Draw joints
    for landmark in landmarks:

        x = int(landmark.x * width)
        y = int(landmark.y * height)

        cv2.circle(
            frame,
            (x, y),
            5,
            (0, 255, 0),
            -1
        )

# ==========================================
# Open Webcam
# ==========================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# ==========================================
# Main Loop
# ==========================================

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert OpenCV image -> MediaPipe Image

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    timestamp = int(time.time() * 1000)

    # Run MediaPipe Tasks inference

    results = hand_landmarker.detect_for_video(
        mp_image,
        timestamp
    )

    left_finger_count = 0
    right_finger_count = 0

    left_wrist_state = "Unknown"
    right_wrist_state = "Unknown"

    # ======================================
    # Process detected hands
    # ======================================

    if results.hand_landmarks:

        for landmarks, handedness in zip(
            results.hand_landmarks,
            results.handedness
        ):

            # Get Left / Right label
            label = handedness[0].category_name

            is_left = label == "Left"


            # Draw hand skeleton
            draw_hand(frame, landmarks)
            # ==================================
            # Finger counting
            # ==================================

            finger_count = 0

            # Thumb detection
            if is_left:

                thumb_up = (
                    landmarks[thumb_tip].x >
                    landmarks[thumb_mcp].x
                )

            else:

                thumb_up = (
                    landmarks[thumb_tip].x <
                    landmarks[thumb_mcp].x
                )


            if thumb_up:
                finger_count += 1


            # Other four fingers
            for tip, pip in zip(
                finger_tips,
                finger_pips
            ):

                if landmarks[tip].y < landmarks[pip].y:
                    finger_count += 1

            # ==================================
            # Open / Closed Hand Detection
            # ==================================

            total_distance = 0


            for tip in [thumb_tip] + finger_tips:

                total_distance += calculate_distance(
                    landmarks[wrist],
                    landmarks[tip]
                )


            average_distance = total_distance / 5


            # Normalise based on hand size because not all people have the same sized hands, this helps to reduce errors

            hand_size = calculate_distance(
                landmarks[wrist],
                landmarks[5]      
            )


            if hand_size > 0:

                normalized_distance = (
                    average_distance /
                    hand_size
                )

            else:

                normalized_distance = 0


            # Threshold
            if normalized_distance > 0.7:

                wrist_state = "Open"

            else:

                wrist_state = "Closed"


            # Store result for each hand

            if is_left:

                left_finger_count = finger_count
                left_wrist_state = wrist_state

            else:

                right_finger_count = finger_count
                right_wrist_state = wrist_state



    # ======================================
    # Display Results
    # ======================================

    cv2.putText(
        frame,
        f"Left Hand - Fingers: {left_finger_count}, Wrist: {left_wrist_state}",
        (10, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )


    cv2.putText(
        frame,
        f"Right Hand - Fingers: {right_finger_count}, Wrist: {right_wrist_state}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )
    window_name = "MediaPipe Tasks Hand Tracking"

    # ======================================
    # Show Camera Feed
    # ======================================

    cv2.imshow(
        "MediaPipe Tasks Hand Tracking",
        frame
    )


    # Quit with q

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break



cap.release()

cv2.destroyAllWindows()

hand_landmarker.close()