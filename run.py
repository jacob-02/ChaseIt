from faceDetection import Face
from Path import pathDetector

count = 0

while True:
    if count % 2 == 0:
        pathDetector.orange()
        count += 1

    else:
        Face.detect('Intruder')
        count += 1
