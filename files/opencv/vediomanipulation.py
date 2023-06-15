#importing the opencv module  
import cv2 as cv
import sys
import os
import numpy as np
# importing datetime module for now()
import datetime as dt
 
# using now() to get current time
current_time = str(dt.datetime.now())



# load vedio from file
#video = cv.VideoCapture('files/opencv/sample.mp4',0)
# it will run the camera 
video = cv.VideoCapture(0)

# status of file or vedio it wil return True or False
print(video.isOpened())

# get the properties of veio frame

print(video.get(cv.CAP_PROP_FRAME_WIDTH))
print(video.get(cv.CAP_PROP_FRAME_HEIGHT))
print(video.get(cv.CAP_PROP_FPS))
print(video.get(cv.CAP_PROP_FRAME_COUNT))

#fourcc is a vedio code .avi *'MP4V'
fourcc = cv.VideoWriter_fourcc(*'XVID')
# to write a vedio ,30 is FPS and width,height(640,480)
output = cv.VideoWriter('New-vedio.avi',fourcc,30,(1280,720))



while (video.isOpened()) :
    # it will read the vedio frame from camera ,ret is boolean True if frame is available 
    ret,frame =video.read()
    
    if ret == True :
        
    
        font = cv.FONT_HERSHEY_SIMPLEX
        video_dim = "Width :" + str(video.get(cv.CAP_PROP_FRAME_WIDTH)) + " Height :" + str(video.get(cv.CAP_PROP_FRAME_HEIGHT)) +" " + current_time
        video_text = cv.putText(frame, video_dim, (300, 700), font, 1, (0,255,0), 1, cv.LINE_AA)           
        cv.imshow("grat Vedio",video_text)

        #for camera value is 1
        key = cv.waitKey(1)

        if key == ord('q'):
            break
    else :
        break

# to release the resources from memory ie camera
video.release()
output.release()
#to destroy all opened windows.
#cv.destroyAllWindow()
