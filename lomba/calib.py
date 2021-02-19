import numpy as np
import cv2
import re
import sys

class calib:
    def __init__(self):
        # Termination criteria
        self.criteria =(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.criteria_stereo= (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # Prepare object points
        self.objp = np.zeros((9*6,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

        # Arrays to store object points and image points from all images
        self.objpoints= []   # 3d points in real world space
        self.imgpointsR= []   # 2d points in image plane
        self.imgpointsL= []

    def start_calib(self, jmlh_gambar):
        # Start calibration from the camera
        print('Starting calibration for the 2 cameras... ')
        # Call all saved images
        for i in range(0,jmlh_gambar):   # Put the amount of pictures you have taken for the calibration inbetween range(0,?) wenn starting from the image number 0
            t= str(i)
            ChessImaR= cv2.imread('chessboard-R'+t+'.png',0)    # Right side
            ChessImaL= cv2.imread('chessboard-L'+t+'.png',0)    # Left side
            retR, cornersR = cv2.findChessboardCorners(ChessImaR,
                                               (9,6),None)  # Define the number of chees corners we are looking for
            retL, cornersL = cv2.findChessboardCorners(ChessImaL,
                                               (9,6),None)  # Left side
            if (True == retR) & (True == retL):
                self.objpoints.append(self.objp)
                cv2.cornerSubPix(ChessImaR,cornersR,(11,11),(-1,-1),self.criteria)
                cv2.cornerSubPix(ChessImaL,cornersL,(11,11),(-1,-1),self.criteria)
                self.imgpointsR.append(cornersR)
                self.imgpointsL.append(cornersL)

        # Determine the new values for different parameters
        #   Right Side
        retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(self.objpoints,
                                                                self.imgpointsR,
                                                                ChessImaR.shape[::-1],None,None)#(::-1)reverse the array
        hR,wR= ChessImaR.shape[:2]
        OmtxR, roiR= cv2.getOptimalNewCameraMatrix(mtxR,distR,(wR,hR),1,(wR,hR))

        #   Left Side
        retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(self.objpoints,
                                                                self.imgpointsL,
                                                                ChessImaL.shape[::-1],None,None)
        hL,wL= ChessImaL.shape[:2]
        OmtxL, roiL= cv2.getOptimalNewCameraMatrix(mtxL,distL,(wL,hL),1,(wL,hL))

        print('Cameras Ready to use')

        retS, MLS, dLS, MRS, dRS, R, T, E, F= cv2.stereoCalibrate(self.objpoints,
                                                                    self.imgpointsL,
                                                                    self.imgpointsR,
                                                                    mtxL,
                                                                    distL,
                                                                    mtxR,
                                                                    distR,
                                                                    ChessImaR.shape[::-1],
                                                                    criteria = self.criteria_stereo,
                                                                    flags= cv2.CALIB_FIX_INTRINSIC)

        # StereoRectify function
        rectify_scale= 0 # if 0 image croped, if 1 image nor croped
        RL, RR, PL, PR, Q, roiL, roiR= cv2.stereoRectify(MLS, dLS, MRS, dRS,
                                                          ChessImaR.shape[::-1], R, T,
                                                            rectify_scale,(0,0))  # last paramater is alpha, if 0= croped, if 1= not croped
        # initUndistortRectifyMap function
        Left_Stereo_Map= cv2.initUndistortRectifyMap(MLS, dLS, RL, PL,
                                                        ChessImaR.shape[::-1], cv2.CV_16SC2)   # cv2.CV_16SC2 this format enables us the programme to work faster
        Right_Stereo_Map= cv2.initUndistortRectifyMap(MRS, dRS, RR, PR,
                                                        ChessImaR.shape[::-1], cv2.CV_16SC2)
        return Left_Stereo_Map, Right_Stereo_Map