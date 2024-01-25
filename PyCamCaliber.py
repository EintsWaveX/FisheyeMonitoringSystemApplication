"""
Camera calibration is a fundamental task in computer vision crucial in various 
applications such as 3D reconstruction, object tracking, augmented reality, and 
image analysis. Accurate calibration ensures precise measurements and reliable 
analysis by correcting distortions and estimating intrinsic and extrinsic camera
parameters. This comprehensive guide delves into the principles, techniques, and
algorithms of camera calibration. We explore obtaining intrinsic and extrinsic 
camera parameters, understanding distortion models, conducting calibration patterns,
and utilizing calibration software. Whether you are a beginner or an experienced
computer vision practitioner, this guide will equip you with the knowledge and
skills to perform accurate camera calibration and unlock the full potential of
your vision-based applications.
"""

# Refer to the original website documentation:
# Author: Analythics Vidhya; All Rights Reserved.
#   > Title: What is Camera Calibration in Computer Vision?
#     Link:  https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-for-camera-calibration-in-computer-vision/

import cv2
import numpy as np
import os
import glob

# Defining the dimensions of checkerboard
CHECKERBOARD: tuple[int, int]    = (6, 9)
criteria: tuple[int, int, float] = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Creating vector to store vectors of 3D points for each checkerboard image
# Creating vector to store vectors of 2D points for each checkerboard image
objpoints, imgpoints = [], []
ret: bool = False

# Defining the world coordinates for 3D points
objp           = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2]   = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

# Extracting path of individual image stored in a given directory
images: list[str] = glob.glob('./images/*.jpg')
for fname in images:
    img  = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    # If desired number of corners are found in the image then ret = true
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD,
    cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    
"""
If desired number of corner are detected,
we refine the pixel coordinates and display
them on the images of checker board
"""
if ret == True:
    objpoints.append(objp)
    
    # Refining pixel coordinates for given 2d points.
    corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
    imgpoints.append(corners2)
    
    # Draw and display the corners
    img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
    cv2.imshow('img',img); cv2.waitKey(0); cv2.destroyAllWindows()
    h, w = img.shape[:2]
    
"""
Performing camera calibration by
passing the value of known 3D points (objpoints)
and corresponding pixel coordinates of the
detected corners (imgpoints)
"""

if __name__ == '__main__':
    try:
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    except NameError:
        print("ERROR (Process):   Camera calibration process has failed for a numerous reasons!")
        print("INFO  (Checking):  Please check your camera status (mainly the Fish Eye camera) are connected")
        print("                   to the computer in order to be able to work with the Computer Vision library.")
        
        print()
        print("NOTE  (Hinting):   Mathematical model of lens distortion covers all sorts of distortions, radial")
        print("                   distortion, decentering distortion, and thin prism distortion, the coefficients")
        print("                   K1 through K6 represent net radial distortion while P1 and P2 represent net")
        print("                   tangential distortion.")
    else:
        print("Camera matrix : n")
        print(mtx)
        print("dist : n")
        print(dist)
        print("rvecs : n")
        print(rvecs)
        print("tvecs : n")
        print(tvecs)