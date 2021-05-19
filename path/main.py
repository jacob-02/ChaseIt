import cv2
import numpy as np
import utlis


def getlanecurve(img):
    imgthresh = utlis.thresholding(img)

    h, w, c = img.shape  # HEIGHT,WIDTH,CHANNELS
    points = utlis.valtrackbars()

    imgwarp = utlis.warpimg(img, points, w, h)

    cv2.imshow("Thresh", imgthresh)
    cv2.imshow('warp', imgwarp)
    return None


if __name__ == '__main__':
    cap = cv2.VideoCapture('Lane.mp4')
    initialtracbarvals = [100, 100, 100, 100]
    utlis.initialisetrackbars(initialtracbarvals)
    while True:
        # utlis.initialisetrackba0rs()
        success, img = cap.read()
        img = cv2.resize(img, (640, 480))
        getlanecurve(img)
        cv2.imshow('Vid', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
