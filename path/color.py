import numpy as np
import cv2

vid = cv2.VideoCapture(0)
coordinates = [[0, 0]]
slope = 0.0

while True:
    ret, image = vid.read()

    hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    yellow_lower = np.array([25, 50, 70], np.uint8)
    yellow_upper = np.array([75, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    kernel = np.ones((5, 5), "uint8")

    yellow_mask = cv2.dilate(yellow_mask, kernel)
    res_yellow = cv2.bitwise_and(image, image, mask=yellow_mask)

    contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 2000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (255, 255, 0), 2)

            cv2.putText(image, "Yellow", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 255, 0))

            centre_x, centre_y = ((x * 2 + w) // 2, (y * 2 + h) // 2)
            x, y = (coordinates[0][0], coordinates[0][1])

            cv2.line(image, (centre_x, centre_y), (coordinates[0][0], coordinates[0][1]), (0, 256, 0))

            if (x-centre_x) != 0.0:
                slope = (y-centre_y)/(x-centre_x)
            cv2.putText(image, str(slope), (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

            coordinates.pop()
            coordinates.append([centre_x, centre_y])

    cv2.imshow("Yellow", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        vid.release()
        cv2.destroyAllWindows()
        break
