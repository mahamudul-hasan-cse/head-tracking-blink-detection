import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Eye blink detection parameters
EYE_AR_THRESH = 0.21
EYE_AR_CONSEC_FRAMES = 2
blink_counter = 0
last_blink_time = 0
blink_cooldown = 0.5

# Eye landmarks for EAR calculation
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def eye_aspect_ratio(eye):
    """
    Calculate the Eye Aspect Ratio (EAR) for blink detection
    """
    # Compute the euclidean distances between the vertical eye landmarks
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    
    # Compute the euclidean distance between the horizontal eye landmarks
    C = np.linalg.norm(eye[0] - eye[3])
    
    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    
    return ear

def landmark_to_np(landmark, w, h):
    return np.array([landmark.x * w, landmark.y * h, landmark.z * w])

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False,
                                  max_num_faces=1,
                                  refine_landmarks=True,
                                  min_detection_confidence=0.5,
                                  min_tracking_confidence=0.5)

# Open camera
cap = cv2.VideoCapture(0)

print("Blink Detection Test")
print("Press 'q' to quit")
print("Blink to trigger mouse click")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0].landmark
        
        # Extract eye landmarks
        left_eye = np.array([landmark_to_np(face_landmarks[i], w, h) for i in LEFT_EYE])
        right_eye = np.array([landmark_to_np(face_landmarks[i], w, h) for i in RIGHT_EYE])
        
        # Calculate EAR for both eyes
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        
        # Average EAR
        ear = (left_ear + right_ear) / 2.0
        
        # Draw eye landmarks
        for i in LEFT_EYE + RIGHT_EYE:
            pt = landmark_to_np(face_landmarks[i], w, h)
            x, y = int(pt[0]), int(pt[1])
            if 0 <= x < w and 0 <= y < h:
                cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)  # Yellow for eye landmarks
        
        # Blink detection logic
        if ear < EYE_AR_THRESH:
            blink_counter += 1
        else:
            if blink_counter >= EYE_AR_CONSEC_FRAMES:
                current_time = time.time()
                if current_time - last_blink_time > blink_cooldown:
                    last_blink_time = current_time
                    print("Blink detected! Clicking mouse...")
                    pyautogui.click()
            blink_counter = 0
        
        # Display EAR value and status on frame
        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Blink Counter: {blink_counter}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Blink to click!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Blink Detection Test", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
