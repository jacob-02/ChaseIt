import cv2


def detector(vid, face_cascade):
        s, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 6)
        a = False
        for (x, y, w, h) in faces:
            a = True
            return a
        vid.release()
        cv2.destroyAllWindows()
        return a
