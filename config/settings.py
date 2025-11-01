class Settings:
    # Camera
    CAMERA_WIDTH = 1280
    CAMERA_HEIGHT = 720
    CAMERA_FPS = 30
    # Violations
    MAX_WARNINGS = 3
    WARNING_COOLDOWN_SEC = 5
    DETECTION_THRESHOLD_FRAMES = 3
    # Gaze
    GAZE_TIMEOUT_SEC = 30
    MAX_GAZE_FAILURES = 4
    # Voice
    TTS_RATE = 150
    # Paths
    VIOLATION_DIR = "violations"
    MODEL_PATH = "models/yolov8n.pt"
