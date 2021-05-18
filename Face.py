import cv2

vid = cv2.VideoCapture(0)


def start(name):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    a = 0
    while True:
        s, img = vid.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.circle(img, ((x+x+w)//2, (y+y+h)//2), 7, (0, 255, 0), thickness=cv2.FILLED)
            print(((x+x+w)//2, (y+y+h)//2))
            a = a + 1
        cv2.imshow(name, img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()


start("Hello")
