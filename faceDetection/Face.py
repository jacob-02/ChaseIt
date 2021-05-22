import cv2


def detect(name):
    slope = 0.0
    count = 0

    vid = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default'
                                                                 '.xml')
    while True:
        s, img = vid.read()
        img = cv2.flip(img, 1)
        height = img.shape[0]
        width = img.shape[1]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 6)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            centre_x, centre_y = ((x + x + w) // 2, (y + y + h) // 2)
            print("X:", centre_x, "Y:", centre_y)

            if (width // 2 - centre_x) != 0:
                slope = (height - centre_y) / (width // 2 - centre_x)

            if 4.0 >= slope > 0.0:
                cv2.putText(img, "Right", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            elif -0.4 >= slope < 0.0:
                cv2.putText(img, "Left", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            else:
                cv2.putText(img, "Front", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        if detector(vid, face_cascade) == 0:
            count += 1
            if count > 20:
                vid.release()
                cv2.destroyAllWindows()
                break

        cv2.imshow(name, img)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break


def detector(vid, face_cascade):
    s, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    a = 0
    for (x, y, w, h) in faces:
        a = 1
        return a
    return a
