import cv2, os
import numpy as np

cascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascadePath)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

cap = cv2.VideoCapture(0)

# recognizer = cv2.createLBPHFaceRecognizer(1,8, 8, 8, 123)
# image_path = {os.path.join(path, f)for f inos
while True:
    success, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.1,5, minSize=(30,30))

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)
        # images.append(image[y: y+labels.append(subject_number
    cv2.imshow("face_rec",img)

    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()