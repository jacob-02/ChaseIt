import cv2
import numpy as np


def thresholding(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 100, 100])
    upper = np.array([30, 200, 220])
    mask = cv2.inRange(img, lower, upper)
    return mask


def warpimg(img, points, w, h):
    pts1 = np.float32(points)
    pts2 = np.float32(([0, 0], [w, 0], [0, h], [w, h]))
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgwarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgwarp


def nothing(a):
    pass


def initialisetrackbars(initialtracbarvals, wT=480, hT=240):
    cv2.namedWindow("trackbars")
    cv2.resizeWindow("trackbars", 360, 240)
    cv2.createTrackbar("width top", "trackbars", initialtracbarvals[0], wT // 2, nothing)
    cv2.createTrackbar("height top", "trackbars", initialtracbarvals[1], hT, nothing)
    cv2.createTrackbar("width bottom", "trackbars", initialtracbarvals[2], wT // 2, nothing)
    cv2.createTrackbar("height bottom", "trackbars", initialtracbarvals[3], hT, nothing)


def valtrackbars(wT=480, hT=240):
    widthtop = cv2.getTrackbarPos("width top", "trackbars")
    heighttop = cv2.getTrackbarPos("height top", "trackbars")
    widthbottom = cv2.getTrackbarPos("width bottom", "trackbars")
    heightbottom = cv2.getTrackbarPos("height bottom", "trackbars")
    points = np.float32([(widthtop, heighttop), (wT - widthtop, heighttop), (widthbottom, heightbottom),
                         (wT - widthbottom, heightbottom)])
    return points
