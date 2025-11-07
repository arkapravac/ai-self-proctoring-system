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
