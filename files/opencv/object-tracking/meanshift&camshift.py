# https://docs.opencv.org/3.4/d7/d00/tutorial_meanshift.html

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read()
# harcascade frontalface
face_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_frontalface_default.xml")

face_rectangle = face_cascade.detectMultiScale(frame,scaleFactor =1.2,minNeighbors=6)


# setup initial location of window
face_x,face_y,width,height=300, 200, 100, 50 # simply hardcoded the values
track_window = (face_x,face_y,width,height)

# set up the ROI for tracking
roi = frame[face_y:face_y+height,face_x:face_x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
roi_histogram = cv.calcHist([hsv_roi],[0],None,[180],[0,180])
cv.normalize(roi_histogram,roi_histogram,0,255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    ret, frame = cap.read()

    if ret==True :
        hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_histogram,[0,180],1)

        # apply meanshift to get the new location
        ret,tracking_window = cv.meanShift(dst,track_window,term_crit)

        face_x,face_y,width,height = tracking_window

        # Draw it on image
        img =cv.rectangle(frame,(face_x,face_y),(face_x+width,face_y+height),255,5)

        cv.imshow("img",img)


        # apply camshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
         # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)
    
        k = cv.waitKey(10) & 0xff
        if k == ord('q'):
            break


cap.release()
cv.destroyWindow()