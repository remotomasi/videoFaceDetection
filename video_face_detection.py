# Source:
# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
#
# Modified and improved by: Remo Tomasi
# remo.tomasi@gmail.com
#

# import the opencv library
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # convert it into gray code from BGR
    # gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

    # apply a scale of 1.1 and 4
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    # Make rectangle around face of green colour and thickness of 3.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
