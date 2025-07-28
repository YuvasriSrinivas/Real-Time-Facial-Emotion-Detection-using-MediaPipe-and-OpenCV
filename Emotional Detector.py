import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Drawing style
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Start video capture
cap = cv2.VideoCapture(0)

# Optional: reduce webcam resolution for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize emotion states
emotion = ''
prev_emotion = ''

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty frame.")
            continue

        # Flip and convert image
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process landmarks
        results = face_mesh.process(rgb_image)

        # Copy image for drawing
        annotated_image = image.copy()
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)

                # Extract coordinates
                landmarks = face_landmarks.landmark
                h, w, _ = image.shape
                mesh_points = np.array([[int(p.x * w), int(p.y * h)] for p in landmarks])

                # Calculate facial distances
                mouth_open = np.linalg.norm(mesh_points[13] - mesh_points[14])
                eye_open = np.linalg.norm(mesh_points[159] - mesh_points[145])
                iris_center = mesh_points[468]
                eye_center = (mesh_points[33] + mesh_points[133]) // 2
                sad_ratio = np.linalg.norm(iris_center - eye_center)

                # Emotion detection logic
                if mouth_open > 15 and eye_open > 10:
                    emotion = "SURPRISED 😲"
                    color = (0, 255, 255)
                elif eye_open < 5 and mouth_open < 5:
                    emotion = "ANGRY 😠"
                    color = (0, 0, 255)
                elif eye_open > 6 and mouth_open > 10:
                    emotion = "HAPPY 😊"
                    color = (0, 255, 0)
                elif sad_ratio > 12:
                    emotion = "SAD 😢"
                    color = (255, 0, 0)
                else:
                    emotion = "NEUTRAL 😐"
                    color = (255, 255, 255)

                # Draw emotion text
                if emotion != prev_emotion:
                    print("Detected Emotion:", emotion)
                    prev_emotion = emotion

                cv2.putText(annotated_image, emotion, (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3, cv2.LINE_AA)

        # Show result
        cv2.imshow('Real-Time Emotion Detection', annotated_image)

        # ESC to quit
        if cv2.waitKey(5) & 0xFF == 27:
            break

        # Optional delay to smooth performance (~30 FPS)
        time.sleep(0.03)

# Release camera
cap.release()
cv2.destroyAllWindows()
