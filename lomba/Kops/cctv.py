'''lebih bagus daripada MOG i think'''


import numpy as np
import cv2

#Alamatnnya apa coba
cap = cv2.VideoCapture ('/home/odroid/Desktop/lomba/Kops/vtest.avi') 
fgbg = cv2.createBackgroundSubtractorKNN()
kernel = cv2.getStructuringElement (cv2.MORPH_ELLIPSE, (3,3))

while (1):
    ret, frame = cap.read()

    fgmask = fgbg.apply (frame)
    
    #Reduce noise
    fgmask = cv2.morphologyEx (fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow ('frame', fgmask)
    k = cv2.waitKey(30) & 0xFF

    if k == ord ('q'):
        break

cap.release()
cv2.destroyAllWindows()
