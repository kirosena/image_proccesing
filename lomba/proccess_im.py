from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import math
import time
import re
import sys

class proccess_im:
    def __init__(self):
        self.kernel= np.ones((6,6),np.uint8)
        #finding_moment
        self.xc=0
        self.yc=0
        self.radius= 0
        self.mx =0
        self.my=0
        self.radius2= 0
        #finding_moment2
        self.xc1=0
        self.yc1=0
        self.radius1= 0
        self.mx1 =0
        self.my1=0
        self.radius2_1= 0
        #finding_moment3
        self.xc2=0
        self.yc2=0
        self.radius2= 0
        self.mx2 =0
        self.my2=0
        self.radius2_2= 0

    def setting_frame_perpektif(self, ret, frame, lx,Stereo_Map):
        # grab the current frame
        ret, frame = lx.read()
        frame= cv2.remap(frame,Stereo_Map[0],Stereo_Map[1], interpolation = cv2.INTER_LANCZOS4, borderMode = cv2.BORDER_CONSTANT)
        #frame = vs.read()
 
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if frame is None:
            pass 
 
        # resize the frame, blur it, and convert it to the HSV
        # color space
        #the frame become 240 height, 320 width
        frame = imutils.resize(frame, width=320)
        #for_checking_the_frame_size
        #check= frame.shape
        #print(check)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        return frame, hsv

    def setting_frame_360(self,ret, frame, lx):
        # grab the current frame
        ret, frame = lx.read()
        #frame = vs.read()
 
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if frame is None:
            pass 
 
        # resize the frame, blur it, and convert it to the HSV
        # color space
        #the frame become 240 height, 320 width
        frame = imutils.resize(frame, width=320)
        #for_checking_the_frame_size
        #check= frame.shape
        #print(check)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        return frame,hsv
    
    def setting_frame_single_camera(self,ret, frame, lx):
        # grab the current frame
        ret, frame = lx.read()
        #frame = vs.read()
 
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if frame is None:
            pass 
 
        # resize the frame, blur it, and convert it to the HSV
        # color space
        #the frame become 240 height, 320 width
        frame = imutils.resize(frame, width=320)
        #for_checking_the_frame_size
        #check= frame.shape
        #print(check)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        return frame,hsv

    def setting_countour_universal(self, hsv, hsvLower, hsvUpper,):
        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, hsvLower, hsvUpper)#detect balls
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, self.kernel)
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #countour ball
        cnts = imutils.grab_contours(cnts)
        return cnts, mask

    def finding_moment(self,cnts, frame):

        if len(cnts) <= 0:
            xc=0
            yc=0
            radius= 0
            frame = frame
            mx =0
            my=0

        else:
            c = max(cnts, key=cv2.contourArea)
            ((xc, yc), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            mx = center[0]
            my = center[1]
            cv2.circle(frame, (int(xc), int(yc)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        return frame, mx, my, radius
    
    def finding_moment_lastpos(self,cnts, frame, mx1, my1, radius):
    
        if len(cnts) <= 0:
            frame = frame

        else:
            c = max(cnts, key=cv2.contourArea)
            ((xc, yc), radius1) = cv2.minEnclosingCircle(c)
            if radius1>10:
                radius = radius1
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                mx1 = center[0]
                my1 = center[1]
                cv2.circle(frame, (int(xc), int(yc)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        return frame, mx1, my1, radius
    
    def finding_moment_lastpos_enemies(self,cnts, frame, mx1, my1, radius):
        
        if len(cnts) <= 0:
            frame = frame
            xc=0
            yc=0
            radius= 0
            mx1 =0
            my1=0

        else:
            c = max(cnts, key=cv2.contourArea)
            ((xc, yc), radius1) = cv2.minEnclosingCircle(c)
            if radius1>20:
                radius = radius1
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                mx1 = center[0]
                my1 = center[1]
                cv2.circle(frame, (int(xc), int(yc)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
            else:
                frame = frame
                xc=0
                yc=0
                radius= 0
                frame = frame
                mx1 =0
                my1=0

        return frame, mx1, my1, radius

    def finding_moment_lastpos_goal(self,cnts, frame):
        
        if len(cnts) <= 0:
            frame = frame

        else:
            c = max(cnts, key=cv2.contourArea)
            ((self.xc2, self.yc2), self.radius2) = cv2.minEnclosingCircle(c)
            if self.radius2>10:
                self.radius2_2 = self.radius2
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                self.mx2 = center[0]
                self.my2 = center[1]
                cv2.circle(frame, (int(self.xc2), int(self.yc2)), int(self.radius2_2),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        return frame, self.mx2, self.my2, self.radius2_2
    
    def display_center_radius(self,frame,xc,yc,radius,xc2,yc2,radius2):
        # loop over the set of tracked points
        cv2.putText(frame, "B dx: {}, dy: {},Dis: {}|En dx: {}, dy: {},Dis: {}".format(int(xc), int(yc),int(radius),int(xc2), int(yc2),int(radius2)),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0, 0, 255), 1)

        return frame

    def derajat_object(self,xc,yc,x_pixel,y_pixel):
        x_calibrate = xc-(x_pixel/2)
        y_calibrate = (y_pixel/2)-yc
        #z_calibrate = math.sqrt((x_calibrate*x_calibrate)+(y_calibrate*y_calibrate))
        if x_calibrate == 0 and y_calibrate >0:
            degreess = -90
        elif x_calibrate > 0 and y_calibrate == 0:
            degreess = 180
        elif x_calibrate == 0 and y_calibrate <0:
            degreess = 90
        elif x_calibrate < 0 and y_calibrate == 0:
            degreess = 0
        elif x_calibrate > 0 and y_calibrate  <0: #kuadran 4
            radianss = math.atan(x_calibrate/y_calibrate)
            degreess = 90 - (math.degrees(radianss))
        elif x_calibrate < 0 and y_calibrate  <0: #kuadran 3
            radianss = math.atan(x_calibrate/y_calibrate)
            degreess = 90 - (math.degrees(radianss))
        elif x_calibrate < 0 and y_calibrate  >0: #kuadran 2
            radianss = math.atan(x_calibrate/y_calibrate)
            degreess = -90 - (math.degrees(radianss))
        else: #kuadran 1
            radianss = math.atan(x_calibrate/y_calibrate)
            degreess = -90 - (math.degrees(radianss))

        degreess_r = np.around(degreess,decimals=2)    
        #print('x_calibrate: '+ str(x_calibrate)+ ' y_calibrate: '+ str(y_calibrate)+ ' degree: '+ str(degreess))
        return degreess_r, x_calibrate, y_calibrate

    def ending_safety(self,vs,vs2,vs3):
        vs.release()
        vs2.release()
        vs3.release()
        print("Finish")
    
        cv2.destroyAllWindows()
    
    def ending_safety_single(self,vs,vs2):
        vs.release()
        vs2.release()
        # vs3.release()
        print("Finish")
    
        cv2.destroyAllWindows()

    def display_grid_360(self,frame3, x_pixel, y_pixel):
        cv2.circle(frame3, (int(x_pixel/2),int(y_pixel/2)), 10, (255, 0, 0), 1)
        cv2.line(frame3,(0,int(y_pixel/2)),(int(x_pixel),int(y_pixel/2)),(255,0,0),1)
        cv2.line(frame3,(int(x_pixel/2),0),(int(x_pixel/2),int(y_pixel)),(255,0,0),1)
        return frame3
