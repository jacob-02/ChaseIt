import numpy as np
import cv2


def orange(vid):
    slope = 0.0

    count = 0

    coordinates = [[0, 0]]
    while True:
        ret, image = vid.read()

        # image = cv2.rotate(image, 0)
        image = image[190:450, 10:1290]

        height = image.shape[0]
        width = image.shape[1]

        image = cv2.GaussianBlur(image, (9, 9), cv2.BORDER_DEFAULT)
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        orange_lower = np.array([5, 50, 50], np.uint8)
        orange_upper = np.array([25, 255, 255], np.uint8)
        orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

        kernel = np.ones((5, 5), "uint8")

        orange_mask = cv2.dilate(orange_mask, kernel)
        res_orange = cv2.bitwise_and(image, image, mask=orange_mask)

        contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y),
                              (x + w, y + h),
                              (25, 255, 255), 2)

                cv2.putText(image, "Orange", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, (255, 255, 0))

                centre_x, centre_y = ((x * 2 + w) // 2, (y * 2 + h) // 2)
                x, y = (coordinates[0][0], coordinates[0][1])

                cv2.line(image, (centre_x, centre_y), (coordinates[0][0], coordinates[0][1]), (25, 255, 255))

                if (x - centre_x) != 0:
                    slope = (y - centre_y) / (x - centre_x)

                if slope > 0.0915:
                    cv2.putText(image, "Right", (width // 2, height // 2), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),
                                3)

                elif slope < -0.0915:
                    cv2.putText(image, "Left", (width // 2, height // 2), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),
                                3)

                # elif slope == 0:
                #     cv2.putText(image, "Left", (width // 2, height // 2), cv2.FONT_HERSHEY_PLAIN, 3,
                #                 (255, 255, 255), 3)

                else:
                    cv2.putText(image, "Straight", (width // 2, height // 2), cv2.FONT_HERSHEY_PLAIN, 3,
                                (255, 255, 255), 3)

                coordinates.pop()
                coordinates.append([centre_x, centre_y])

        cv2.imshow("images", np.hstack([image, res_orange]))

        count += 1

        if count > 280:
            vid.release()
            cv2.destroyAllWindows()
            break

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
