import cv2
import mediapipe as mp
import math
import winsound
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ================= CONFIG =================
EAR_THRESHOLD = 0.28
CONSEC_FRAMES = 15
counter = 0
alert_triggered = False

# ================= EAR FUNCTIONS =================
def euclidean(p1, p2):
    return math.dist(p1, p2)

def calculate_ear(eye):
    A = euclidean(eye[1], eye[5])
    B = euclidean(eye[2], eye[4])
    C = euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# ================= MEDIAPIPE SETUP =================
base_options = python.BaseOptions(model_asset_path="face_landmarker.task")
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    num_faces=1
)
detector = vision.FaceLandmarker.create_from_options(options)

# ================= VIDEO CAPTURE =================
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]

        left_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in LEFT_EYE]
        right_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in RIGHT_EYE]

        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        ear = (left_ear + right_ear) / 2.0

        for p in left_eye + right_eye:
            cv2.circle(frame, p, 2, (0, 255, 0), -1)

        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        # ========== DROWSINESS LOGIC ==========
        if ear < EAR_THRESHOLD:
            counter += 1
            if counter >= CONSEC_FRAMES and not alert_triggered:
                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    3
                )
                winsound.Beep(1000, 800)
                alert_triggered = True
        else:
            counter = 0
            alert_triggered = False

        cv2.putText(
            frame,
            f"Counter: {counter}",
            (30, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

    cv2.imshow("Drowsiness Predictor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
