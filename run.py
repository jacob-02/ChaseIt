from faceDetection import Face
from Path import pathDetector
import cv2

count = 0


while True:
    if count % 2 == 0:
        vid = cv2.VideoCapture('robo2.mp4')
        pathDetector.orange(vid)
        count += 1

    else:
        Face.detect('Intruder')
        count += 1
