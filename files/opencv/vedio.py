#importing the opencv module  
import cv2 as cv
import sys
import os
import numpy as np

# load vedio from file
video = cv.VideoCapture('files/opencv/sample.mp4',0)
# it will run the camera 
#video = cv.VideoCapture(0)

# status of file or vedio it wil return True or False
print(video.isOpened())

while (video.isOpened()) :
    # it will read the vedio frame from camera
    ret,frame =video.read()

    #convert BGR vedio frame to Gray 
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #convert BGR vedio frame to RGB
    rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    #it will run the vedio frame on window
    cv.imshow("My Vedio",gray)

    #for camera value is 1
    key = cv.waitKey(1)

    if key == ord('q') :
        break

# to release the resources from memory ie camera
video.release()
#to destroy all opened windows.
cv.destroyAllWindow()
