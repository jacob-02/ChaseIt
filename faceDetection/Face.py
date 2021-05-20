import time
import cv2


def detect(name):

    count = 0

    vid = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default'
                                                                 '.xml')
    if detector(vid, face_cascade) == 1:
        while True:
            s, img = vid.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.2, 6)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                centre_x, centre_y = ((x + x + w) // 2, (y + y + h) // 2)
                print(centre_x, centre_y)

            count += 1

            if detector(vid, face_cascade) == 0 or count > 200:
                vid.release()
                cv2.destroyAllWindows()
                break

            cv2.imshow(name, img)

            if cv2.waitKey(20) & 0xFF == ord('d'):
                vid.release()
                cv2.destroyAllWindows()
                break


def detector(vid, face_cascade):
    s, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    a = 0
    for (x, y, w, h) in faces:
        a = 1
        return a
    vid.release()
    cv2.destroyAllWindows()
    return a
