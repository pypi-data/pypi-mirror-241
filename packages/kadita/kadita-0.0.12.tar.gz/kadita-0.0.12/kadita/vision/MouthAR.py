import cv2
from scipy.spatial import distance


class MouthDetector:
    def __init__(self):
        pass

    @staticmethod
    def calculate_mouth_aspect_ratio(mouth):
        A = distance.euclidean(mouth[13], mouth[19])
        B = distance.euclidean(mouth[14], mouth[18])
        C = distance.euclidean(mouth[15], mouth[17])
        D = distance.euclidean(mouth[12], mouth[16])
        mar = (A + B + C) / (2 * D)
        return mar
