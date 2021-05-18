import cv2
import pickle
import sys
import test


def reco():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    conf_min = 45
    conf_max = 85
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    with open("labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        print(frame.shape)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            id_, conf = recognizer.predict(roi_gray)
            if conf_min <= conf <= conf_max:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                temp = conf - conf_min
                cp = 100 - int((temp / conf_min) * 100)
                if cp > 73:
                    print(test.find(name))
                    a = cv2.imread('images/download.jpeg')
                    cv2.imshow("Ordered", a)
                    cv2.waitKey(6000)
                    cv2.destroyAllWindows()
                    sys.exit()
                cv2.putText(frame, str(cp) + "%", (x, y - 30), font, 1, color, stroke, cv2.LINE_AA)

        cv2.imshow('ironman', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()


reco()
