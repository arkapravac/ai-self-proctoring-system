import mediapipe as mp
class GazeTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
    def get_landmarks(selfs,rgb_frame):
        results.face_mesh.process(rbg_frame)
        return results.multi_face_landmarks[0] if results.multi_face_landmarks else None

    def is_looking_at_screen(self, landmarks):
        if not landmarks:
            return False

            l_iris_x = landmarks.landmark[468].x
            r_iris_xr_iris_x = landmarks.landmark[473].x
            l_left, l_right = landmarks.landmark[130].x, landmarks.landmark[133].x
            r_left, r_right = landmarks.landmark[362].x,landmarks.landmark[263].x
