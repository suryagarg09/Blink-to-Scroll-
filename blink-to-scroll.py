import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Constants for blink detection
LEFT_EYE_TOP = 386
LEFT_EYE_BOTTOM = 374
EAR_THRESHOLD = 4.5     # Lower = tighter blink sensitivity
CONSEC_FRAMES = 2       # Frames eyes must stay closed to count as a blink

blink_counter = 0
blink_active = False
last_blink_time = 0
cooldown = 1.2  # seconds

def euclidean_distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        top = landmarks[LEFT_EYE_TOP]
        bottom = landmarks[LEFT_EYE_BOTTOM]

        eye_dist = euclidean_distance(top, bottom) * frame.shape[0]

        current_time = time.time()

        # Detect blink
        if eye_dist < EAR_THRESHOLD:
            blink_counter += 1
        else:
            if blink_counter >= CONSEC_FRAMES and not blink_active and current_time - last_blink_time > cooldown:
                print("Blink confirmed → Scrolling")
                pyautogui.scroll(-500)
                blink_active = True
                last_blink_time = current_time
            blink_counter = 0
            blink_active = False

    cv2.imshow("Eye Blink Scroll", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
