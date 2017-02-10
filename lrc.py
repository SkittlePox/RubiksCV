import numpy as np
import cv2
from Tkinter import *
import tkMessageBox
import controls

def thinContours(cnts, sensitivity, area):
    newcnts = []
    for c in cnts:
    	# approximate the contour
    	peri = cv2.arcLength(c, True)
    	approx = cv2.approxPolyDP(c, sensitivity * peri, True)

    	# if our approximated contour has four points, then
    	# we can assume that we have found our screen
    	if len(approx) == 4 and cv2.contourArea(approx) > area:
    		newcnts.append(approx)
    return newcnts

# Webcam
cap = cv2.VideoCapture(1)

# Controls
controls.init()

# Color Variables
r1 = np.array([156, 220, 65])   #Dark Red
r2 = np.array([180, 250, 110])

while(True):
    # Controls
    c, t1, t2, blur, erode_iterations, poly, cntrarea = controls.main()
    r1 = t1
    r2 = t2

    # Capture frame-by-frame
    ret, im = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, r1, r2)

    mask = cv2.GaussianBlur(mask, (blur,blur), 0)
    mask = cv2.erode(mask, (3, 3), iterations=erode_iterations)
    _, contours, _= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = thinContours(contours, poly, cntrarea)

    cv2.drawContours(im, contours, -1, (0, 255, 0), 1)

    # Display the resulting frame
    cv2.imshow('frame',im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print r1,r2
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
