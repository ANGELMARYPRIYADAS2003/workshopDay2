import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Point between eyebrows
            center_point_id = 168

            h, w, _ = frame.shape
            point = face_landmarks.landmark[center_point_id]

            cx, cy = int(point.x * w), int(point.y * h)

            # Move the dot slightly upward (change -8 to adjust height)
            cv2.circle(frame, (cx, cy - 20), 10, (0, 0, 255), -1)

    cv2.imshow("Face Dot", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
