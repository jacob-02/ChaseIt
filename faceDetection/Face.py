import cv2
import detector
import pathDetector


def start(name):
    vid = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default'
                                                                 '.xml')
    while True:
        s, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 6)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            centre_x, centre_y = ((x + x + w) // 2, (y + y + h) // 2)
            print(centre_x, centre_y)

        cv2.imshow(name, img)

        if not detector.detector(vid, face_cascade):
            video = cv2.VideoCapture(0)
            pathDetector.yellow(video)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()


start('Intruder')

