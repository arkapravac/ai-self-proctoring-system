import cv2
lass Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self._setup()
