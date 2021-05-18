import cv2

vid = cv2.VideoCapture(0)


def start(name):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    a = 0
    while True:
        s, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            a = a + 1
        cv2.imshow(name, img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()


start("Hello")
