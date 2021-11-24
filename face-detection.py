# Source:
# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
#

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('people.jpg')
# convert it into gray code from BGR
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply a scale of 1.1 and 4
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Make rectangle around face of green colour and thickness of 3.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
