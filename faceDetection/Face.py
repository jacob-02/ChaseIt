import cv2
import detector


def start(name, vid, face_cascade):
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    while True:
        s, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 6)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            centre_x, centre_y = ((x + x + w) // 2, (y + y + h) // 2)
            cv2.circle(img, (centre_x, centre_y), 7, (0, 255, 0), thickness=cv2.FILLED)
            slope = (height - centre_y) // (width // 2 - centre_x)
            print(centre_x, centre_y)
            if 4.0 >= slope > 0.0:
                cv2.putText(img, "Left", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            elif -0.4 >= slope < 0.0:
                cv2.putText(img, "Right", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            else:
                cv2.putText(img, "Front", (280, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        cv2.imshow(name, img)

        if not detector.detector(vid, face_cascade):
            break

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
