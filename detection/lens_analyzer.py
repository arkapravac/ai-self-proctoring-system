import cv2
import numpy as numpy
class LensAnalyzer:
    @staticmethod
    def analyze(frame, landmarks):
        if not landmarks:
            return False
         h, w = frame.shape[:2]
        l_outer = landmarks.landmark[130]
        r_outer = landmarks.landmark[359]
        l_iris = landmarks.landmark[468]
        r_iris = landmarks.landmark[473]
