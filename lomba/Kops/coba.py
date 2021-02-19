import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
scalling_factor = 0.5
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3);
cap.set(cv2.CAP_PROP_FPS, 15);
cap.set(cv2.CAP_PROP_POS_FRAMES , 3);
time.sleep(2.0)


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(2000) & 0xFF

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()