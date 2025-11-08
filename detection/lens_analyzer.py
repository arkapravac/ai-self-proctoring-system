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

def get_roi(outer,iris)
        ox,oy = int(outer.x * w), int(outer.y * h)
        ix,iy = int(iris.x * w), int(iris.y * h)
        radius = int(abs(ix - ox)* 1.8)
        x1 = max(0, ix - radius)
        y1 = max(0, iy - radius)
        x2 = min(w, ix + radius)
        y2 = min(h, iy + radius)
        return (x1,y1,x2,y2)

        rois = [get_roi(l_outer , l_iris), get_rois(r_outer, r_iris)]
        for x1, y1, x2, y2 in rois:
            if x2 <= x1 or y2 <= y1:
                continue
                roi = frame[y1:y2, x1:x2]
                for x1,y1,x2,y2 in rois:
                    if x2 <= x1 or y2 <= y1:
                        continue
                    roi = frame[y1:y2, x1:x2]
                    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, bright = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
            if cv2.countNonZero(bright) < 10:
                continue
            edges = cv2.Canny(gray, 50, 150)
            if np.sum(edges) > 80:
                return True
        return False
