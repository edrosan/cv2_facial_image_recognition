from importlib.resources import path
import cv2

clasificador = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(clasificador)


https://unsplash.com/photos/wOErEtH_c9s
img = cv2.imread('./src/t.png')
faces = face_cascade.detectMultiScale(img)

for(x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2 )

cv2.imshow("Deteccion Facial", img)
cv2.waitKey(0)