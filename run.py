from faceDetection import Face
from Path import pathDetector
import cv2


while True:
    vid = cv2.VideoCapture('TASK_3.mp4')
    pathDetector.orange(vid)
    Face.detect('Intruder')
