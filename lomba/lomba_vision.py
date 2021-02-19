#from collections import deque
#import argparse
#from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
#import math
import time
#modul_buatan_sendiri
#from calib import calib
#from Frame_Angles import Frame_Angles
from proccess_im import proccess_im
import re
from image_decision import decision
import OdroidSerial
from multiprocessing import Queue,Process

#setting_lower_and_upper_HSV_bola_oren

#setting for tag purple
# enemieslower = (144,16,0)
# enemiesupper = (188,255,255)

# #setting for tag purple
# enemieslower = (135,12,57)
# enemiesupper = (188,153,200)
#new_tag 201
enemieslower = (123,46,20)
enemiesupper = (185,218,141)
 #declare UART
ser = OdroidSerial.Serial()

#carton_oren
# greenLower = (2, 178, 58)
# greenUpper = (41, 255, 255)

#karton_oren_malem_kontrakan
# greenLower = (0, 179, 109)
# greenUpper = (21, 255, 255)

#bola_oren_siang_kontrakan
# greenLower = (2, 130, 109)
# greenUpper = (25, 255, 255)

#bola_oren_kelas_201A
# greenLower = (2, 70, 93)
# greenUpper = (44, 255, 255)
#bola_oren_kelas_203_aman_grepes #(2, 125, 59)
# greenLower = (2, 125, 59) 
# greenUpper = (51, 255, 255)

greenLower = (2, 130, 99) 
greenUpper = (51, 255, 255)

#bola_oren_360
greenLower_360 = (2, 128, 103)
greenUpper_360 = (47, 200, 255)

#Gawang_Biru
# gLower = (98, 83, 123)
# gUpper = (125, 255, 255)

#Gawang_Biru_201_arah gawang
# gLower = (98, 83, 123)
# gUpper = (127, 255, 255)

#Gawang_Biru_201_arah lawan gawang
#gLower = (98, 83, 99)
#gUpper = (127, 255, 255)

#parameter global setting_countour
cnts = None
ret = None
frame = None
mask = None

# #parameter_pendukung
# # cameras variables
# left_camera_source = 1
# right_camera_source = 2
pixel_width = 320
pixel_height = 240
# angle_width = 60
# angle_height = 46.826 
#frame_rate = 20
# camera_separation = 14
#parameter_for_line_circle
x_pixel = 320
y_pixel = 240

# setting_camera1_left
vs = cv2.VideoCapture(1)#kiri
vs.set(3,640)
vs.set(4,480)
vs.set(cv2.CAP_PROP_BUFFERSIZE, 3);
vs.set(cv2.CAP_PROP_FPS, 30);
vs.set(cv2.CAP_PROP_POS_FRAMES , 3);
time.sleep(2.0)

# #setting_camera2_right
# vs2 = cv2.VideoCapture(1)#kanan
# vs2.set(3,640)
# vs2.set(4,480)
# vs2.set(cv2.CAP_PROP_BUFFERSIZE, 3);
# vs2.set(cv2.CAP_PROP_FPS, 30);
# vs2.set(cv2.CAP_PROP_POS_FRAMES , 3);
# time.sleep(2.0)

#setting_camera_360
vs3 = cv2.VideoCapture(0)
vs3.set(3,640)
vs3.set(4,480)
vs3.set(cv2.CAP_PROP_BUFFERSIZE, 3);
vs3.set(cv2.CAP_PROP_FPS, 30);
vs3.set(cv2.CAP_PROP_POS_FRAMES , 3);
time.sleep(2.0)

#calibrate_camera
# start = time.perf_counter()
# cal= calib()
# Left_Stereo_Map, Right_Stereo_Map = cal.start_calib(30)#sum_of_sample_camera
# finish = time.perf_counter()
# print(f'Finished in {round(finish-start,4)} seconds')
# #buildframe
# angler = Frame_Angles(pixel_width,pixel_height,angle_width,angle_height)
# angler.build_frame()

distance = 0
process =  proccess_im()
dec = decision()
#paramater_movement
cond = 0
cond2 = 0
en_cond = 0
#parameter list
mx1_b = my1_b = radius1_b = 0 
mx2_b = my2_b = radius2_b = 0
mx1_e = my1_e = radius1_e = 0
mx2_e = my2_e = radius2_e = 0
mx1_g = my1_g = radius1_g = 0
mx2_g = my2_g = radius2_g = 0
mx3_b = my3_b = radius3_b = 0
mx3_e = my3_e = radius3_e = 0
# key = " "
def kirimRasp(q,ser):
    Kord = [0,0,0] #Kord[0] = X ; Kord[1] = radius ; Kord[2] = degreBall
    [kordX,radius,degreBall]=[0,0,0]
    while True:
        while q.empty() is False:
            Kord = q.get()
            # print(Kord)
        if kordX != Kord[0] or radius != Kord[1] or degreBall != Kord[2]:
            ser.write(int(Kord[0]),int(Kord[1]),int(Kord[2]))
            print([Kord[0],Kord[1],Kord[2]])
            [kordX,radius,degreBall] = [Kord[0],Kord[1],Kord[2]]
        time.sleep(0.1)

Kord = [0,0,0,0,0] #Kord[0] = X ; Kord[1] = radius ; Kord[2] = degreBall
[cond_b,cond_g,jrk_b, jrk_e,jrk_g]=[0,0,0,0,0]

def kirimRasp_live(ser,get):
    global Kord, cond_b,cond_g,jrk_b, jrk_e,jrk_g
    Kord = get
    # print(Kord)
    if cond_b != Kord[0] or cond_g != Kord[1] or jrk_b != Kord[2] or jrk_e != Kord[3] or jrk_g != Kord[4]:
        ser.write2(int(Kord[0]),int(Kord[1]),int(Kord[2]),int(Kord[3]),int(Kord[4]))
        #print([Kord[0],Kord[1],Kord[2]])
        [cond_b,cond_g,jrk_b,jrk_e,jrk_g] = [Kord[0],Kord[1],Kord[2],Kord[3],Kord[4]]
# q=Queue()
# p2 = Process(target=kirimRasp,args=(q,ser))
# if __name__ == '__main__': 
# 	p2.start()
def coordinate_mouse(event,x,y,flags,param):
    # print('ok')
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x = {x}, y = {y}')

try:
    while True:
        start = time.perf_counter()
        #setting frame

        #frame1, hsv1 = process.setting_frame_perpektif(ret, frame, vs, Left_Stereo_Map) #kiri
        frame1, hsv1 = process.setting_frame_single_camera(ret, frame, vs)
        # frame2, hsv2 = process.setting_frame_perpektif(ret, frame, vs2, Right_Stereo_Map)#kanan
        frame3, hsv3 = process.setting_frame_360(ret, frame, vs3)

        #setting_mask
        cnts1_b, mask1_b = process.setting_countour_universal(hsv1,greenLower, greenUpper)#ball_masking_kamera_perpekstif
        # cnts2_b, mask2_b = process.setting_countour_universal(hsv2,greenLower, greenUpper)#ball_masking_kamera_360_perpekstif
        # cnts1_e, mask1_e = process.setting_countour_universal(hsv1,enemieslower, enemiesupper)#enemies_masking_kamera_perpekstif
        # cnts2_e, mask2_e = process.setting_countour_universal(hsv2,enemieslower, enemiesupper)#enemies_masking_kamera_360_perpekstif
        # cnts1_g, mask1_g = process.setting_countour_universal(hsv1,gLower, gUpper)#enemies_masking_kamera_perpekstif
        # cnts2_g, mask2_g = process.setting_countour_universal(hsv2,gLower, gUpper)#enemies_masking_kamera_360_perpekstif

        cnts3_b, mask3_b = process.setting_countour_universal(hsv3,greenLower_360, greenUpper_360)#ball_masking_kamera_360
        # cnts3_e, mask3_e = process.setting_countour_universal(hsv3,enemieslower, enemiesupper)#enemies_masking_kamera_360

        #finding_moment
        frame1, mx1_b, my1_b, radius1_b = process.finding_moment_lastpos(cnts1_b, frame1, mx1_b, my1_b, radius1_b)
        # frame2, mx2_b, my2_b, radius2_b = process.finding_moment_lastpos(cnts2_b, frame2, mx2_b, my2_b, radius2_b)
        # frame1, mx1_e, my1_e, radius1_e = process.finding_moment_lastpos_enemies(cnts1_e, frame1, mx1_e, my1_e, radius1_e)
        # frame2, mx2_e, my2_e, radius2_e = process.finding_moment_lastpos_enemies(cnts2_e, frame2, mx2_e, my2_e, radius2_e)
        # frame1, mx1_g, my1_g, radius1_g = process.finding_moment_lastpos(cnts1_g, frame1, mx1_g, my1_g, radius1_g)
        # frame2, mx2_g, my2_g, radius2_g = process.finding_moment_lastpos(cnts2_g, frame2, mx2_g, my2_g, radius2_g)
        frame3, mx3_b, my3_b, radius3_b = process.finding_moment(cnts3_b, frame3)#ball_moment
        # frame3, mx3_e, my3_e, radius3_e = process.finding_moment(cnts3_e, frame3)#ball_moment

        # finding distance ball
        if len(cnts1_b)<=0:
            distance_ball = 0
            # print('sebelah hilang')
        elif 233<=mx1_b<=320 and (((-mx1_b+320)/87)*240)<=my1_b:
            distance_ball = 0
            # print('masuk kanan')
        elif 0<=mx1_b<=87 and (-mx1_b*240/87*-1)<=my1_b:
            distance_ball = 0
            # print('masuk kiri')
        else:
            if my1_b < 188:
                distance_ball = round((-0.0117*(radius1_b**3)) + (1.2768*(radius1_b**2)) - (48.191*radius1_b) + 743.52)
            else:
                distance_ball = 0

        #     xlangle_b,ylangle_b = angler.angles_from_center(mx1_b,my1_b,top_left=True,degrees=True)
        #     xrangle_b,yrangle_b = angler.angles_from_center(mx2_b,my2_b,top_left=True,degrees=True) 
        #     B_X,B_Y,B_Z,B_D = angler.location(camera_separation,(xlangle_b,ylangle_b),(xrangle_b,yrangle_b),center=True,degrees=True)

        # #finding distance goal
        # if len(cnts1_g)<=0 or len(cnts2_g)<=0:
        #     G_X,G_Y,G_Z,G_D = 0,0,0,0
        #     # print('sebelah hilang')
        # elif 233<=mx1_g<=320 and (((-mx1_g+320)/87)*240)<=my1_g:
        #     G_X,G_Y,G_Z,G_D = 0,0,0,0
        #     # print('masuk kanan')
        # elif 0<=mx2_g<=87 and (-mx2_g*240/87*-1)<=my2_g:
        #     G_X,G_Y,G_Z,G_D = 0,0,0,0
        #     # print('masuk kiri')
        # else:
        #     xlangle_g,ylangle_g = angler.angles_from_center(mx1_g,my1_g,top_left=True,degrees=True)
        #     xrangle_g,yrangle_g = angler.angles_from_center(mx2_g,my2_g,top_left=True,degrees=True)
        #     G_X,G_Y,G_Z,G_D = angler.location(camera_separation,(xlangle_g,ylangle_g),(xrangle_g,yrangle_g),center=True,degrees=True)            
        
        # triangulate
        # B_X,B_Y,B_Z,B_D = angler.location(camera_separation,(xlangle_b,ylangle_b),(xrangle_b,yrangle_b),center=True,degrees=True)
        # E_X,E_Y,E_Z,E_D = angler.location(camera_separation,(xlangle_e,ylangle_e),(xrangle_e,yrangle_e),center=True,degrees=True)
        # G_X,G_Y,G_Z,G_D = angler.location(camera_separation,(xlangle_g,ylangle_g),(xrangle_g,yrangle_g),center=True,degrees=True)
        
        # xlangle_e,ylangle_e = angler.angles_from_center(mx1_e,my1_e,top_left=True,degrees=True)
        # xrangle_e,yrangle_e = angler.angles_from_center(mx2_e,my2_e,top_left=True,degrees=True)
        # E_X,E_Y,E_Z,E_D = angler.location(camera_separation,(xlangle_e,ylangle_e),(xrangle_e,yrangle_e),center=True,degrees=True)

        # distance_ball = np.around(B_Z,decimals=2)
        # distance_enemies = np.around(E_Z,decimals=2)
        # distance_goal = np.around(G_Z,decimals=2)
        #distance_ball, distance_enemies, distance_goal = dec.distance_calib(int(distance_ball), int(distance_enemies), int(distance_goal),cnts1_b,cnts2_b,cnts1_e,cnts2_e,cnts1_g,cnts2_g)
        # print(f'jarak bola= {distance_ball} jarak goal ={distance_goal} jarak enemies= {distance_enemies}')

        #displaying_coordinat_on_frame
        # frame1 = process.display_center_radius(frame1, mx1_b, my1_b,distance_ball,mx1_e, my1_e,distance_enemies)
        # frame2 = process.display_center_radius(frame2, mx2_b, my2_b,distance_ball,mx2_e, my2_e,distance_enemies)
        # frame3 = process.display_center_radius(frame3, mx3_b, my3_b,radius3_b,mx3_e, my3_e,radius3_e)
        # frame3 = process.display_grid_360(frame3,x_pixel,y_pixel)

        #mencari derajat
        degree_ball, x_point_b, y_point_b = process.derajat_object(mx3_b, my3_b,x_pixel,y_pixel )
        # degree_enemies, x_point_e, y_point_e = process.derajat_object(mx3_e, my3_e,x_pixel,y_pixel)
        #print(f'derajat ball = {degree_ball} derajat enemies = {degree_enemies}')
        #grid_straight
        # cv2.line(frame1,(112,int(240)),(int(168),int(81)),(255,0,0),1)
        # cv2.line(frame1,(242,int(240)),(int(184),int(81)),(255,0,0),1)

        #display_view_camera
        #cv2.imshow("Kanan_mask", mask1)
        # cv2.imshow("kiri", frame1)
        # print(distance_ball)
        # #cv2.imshow("Kiri_Mask2", mask2)
        # cv2.imshow("kanan", frame2)
        #cv2.imshow("kamera 360 mask", mask3)
        #cv2.imshow("kamera 360", frame3)
        # cv2.setMouseCallback("kiri",coordinate_mouse,frame1)
        cond = dec.straight_condition_letfhi(mx1_b,my1_b,cnts1_b)
        # cond2 = dec.straight_condition_4(mx1_e,my1_e,cnts1_e)
        # cond2 = dec.straight_condition_1(mx1_g,mx2_g, my1_g,my2_g,cnts1_g,cnts2_g)
        # en_cond = dec.straight_condition_1(mx1_e,mx2_e, my1_e,my2_e,cnts1_e,cnts2_e)
        # if en_cond is 1 and distance_enemies <150:
        #     cond = 4
        #     cond2 = 4
        if radius1_b <10:
            cond = 0
        
        #q.put([int(cond),int(distance_ball),int(distance_enemies)])

        if len(cnts1_b) <= 0:
            radius1_b = 0
            cond = 0

        # distance_ball = int(radius1_b)
        degree_ball = int(degree_ball) 
        # distance_enemies = int(radius1_e)
        # degree_enemies = int(degree_enemies)

        # fDegreeBall = degree_ball
        data_kirim = [cond, distance_ball,degree_ball,mx1_b, my1_b]
        # data_kirim = [int(cond),int(distance_enemies),int(distance_ball),int(degree_ball),int(degree_enemies)]
        # print(['\t\t\t\t\t\t\t                                          ',int(cond),int(distance_ball),int(degree_ball),int(mx1_b),int(my1_b)])
        kirimRasp_live(ser,data_kirim)
        # print(mx1_b, my1_b)
        # print(mx1_b, my1_b)
        # if the 'q' key is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            process.ending_safety_single(vs,vs3)
            print("finish")
            # p2.terminate()
            break

        # print('\t\t\t\t\t\t\t',distance_ball,' ', degree_ball, ' ', cond)
        # print('\t\t\t\t\t\t\t\t X= ', B_X, ' Y= ', B_Y)
        # print('\t\t\t\t\t\t\t\t',cond)
        # print('\t\t\t\t\t\t\t\t', my1_b)
        finish = time.perf_counter()
        # print(f'\t\t\t\t\t\t\tFinished in {round(finish-start,4)} seconds')
        #print(distance_ball)

except KeyboardInterrupt:
    # p2.terminate()    
    process.ending_safety_single(vs,vs3)
    print("finish")
    

