from collections import deque
#from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
x_pixel = 640
y_pixel = 480
cap= cv2.VideoCapture(1)
cap.set(3,x_pixel)#width pixel
cap.set(4,y_pixel)#height pixel
cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_POS_FRAMES , 1)
try:
    while (True):

        # capture frame by frame
        ret, frame = cap.read()
        #our operation on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.circle(frame, (int(x_pixel/2),int(y_pixel/2)), 10, (255, 0, 0), 1)
        cv2.line(frame,(0,int(y_pixel/2)),(int(x_pixel),int(y_pixel/2)),(255,0,0),1)
        cv2.line(frame,(int(x_pixel/2),0),(int(x_pixel/2),int(y_pixel)),(255,0,0),1)
        # DISPLAY THE RESULTING FRAME
        print("ready")
        #cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    #when every thing done, release the capture
    cap.release()
    cv2.destroyAllWindows()


