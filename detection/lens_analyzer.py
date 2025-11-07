import cv2
import numpy as numpy
class LensAnalyzer:
    @staticmethod
    def analyze(frame, landmarks):
        if not landmarks:
            return False
