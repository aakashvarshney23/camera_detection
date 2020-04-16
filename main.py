import cv2
import time

face_cascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

# the value 0 states that we are using integrated camera.
# If we cannot detect the camera module, might wanna change this parameter
captured_image = cv2.VideoCapture(0)
result = True

while result:

    ret, img = captured_image.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        #eye_color = img[y:y + h, x:x + w]
        face_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    #time.sleep(3)

    cv2.imwrite("Storage/captd_image.jpg", img)
    #result = False

captured_image.release()
cv2.destroyAllWindows()