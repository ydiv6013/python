# tracking using different opencv APIs

import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

# status of file or vedio it wil return True or False
status =video.isOpened()

# read the first frame
ret,frame = video.read()

# special function to draw inital frame at desired ROI
roi =cv.selectROI(frame,showCrosshair=False)

# initialize tracker with first frame and bouding box
tracker1= cv.TrackerBoosting_create()
tracker2 = cv.TrackerMIL_create()
tracker3 = cv.TrackerKCF_create()
tracker4 = cv.TrackerTLD_create()
tracker5 = cv.TrackerMedianFlow_create()

print(tracker1)
print(tracker2)
print(tracker3)
print(tracker4)
print(tracker5)
tracker_name = str(tracker1).split[0][1:]

ret = tracker1.init(frame,roi)
while status == True :
    # read a new Frame
    ret,frame =video.read()
    # update tracker
    success , roi = tracker1.update(frame)

    (x,y,w,h) = tuple(int,roi)
    if success :
        p1 = (x,y)
        p2 = (x+w,y+h)
        cv.rectangle(frame,p1,p2,(0,255,0),3)
    else :
        # tracking failure
        cv.putText(frame,"Failure to Detect",(100,200),cv.FONT_HERSHEY_COMPLEX,10,(0,255,0),5)

    #display tracker type on frame
    cv.putText(frame,tracker_name,(20,400),cv.FONT_HERSHEY_COMPLEX,10,(0,255,0),5)

    # display result
    cv.imshow(tracker_name,frame)

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break


# to release the resources from memory ie camera
video.release()