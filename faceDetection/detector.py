import cv2


def detector():
    vid = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        s, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 6)
        a = False
        for (x, y, w, h) in faces:
            a = True
            return a

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
    return a
