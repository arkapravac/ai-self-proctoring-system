import cv2
class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self._setup()
    def _setup(self):
        s = Settings
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,s.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, s.CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS,s.CAMERA_FPS)
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
        self.cap.net(cv2.CAP_PROP_EXPOSURE, -4)
        self.cap.net(cv2.CAP_PROP_BRIGHTNESS, 128)
        self.cap.net(cv2.CAP_PROP_CONTRAST, 64)
    def read(self):
        return self.cap.read()
    def release(self):
        self.cap.release()