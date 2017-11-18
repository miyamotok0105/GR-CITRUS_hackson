#python2
#
#python haarcascade_any.py meta_data/haarcascade_eye.xml

import cv2
import sys

img = cv2.imread('sample.jpg')

cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Draw a rectangle around the faces

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("face hit!!!")
    print(x, ":",y, ":", x+w, ":", y+h)
    
if len(faces) == 0:
    print("face is not hit")
    