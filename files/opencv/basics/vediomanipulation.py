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

width = video.get(cv.CAP_PROP_FRAME_WIDTH)
height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
print(video.get(cv.CAP_PROP_FPS))
print(video.get(cv.CAP_PROP_FRAME_COUNT))

#fourcc is a vedio code .avi *'MP4V'
fourcc = cv.VideoWriter_fourcc(*'XVID')
# to write a vedio ,30 is FPS and width,height(640,480)
output = cv.VideoWriter('New-vedio.avi',fourcc,30,(1280,720))


# global variables to draw a rectangle
pt1 =(0,0)
pt2 =(0,0)
topleft_clicked = False
bottomright_clicked = False

# callback function

def draw_rectangle(event,x,y,flags,param) :
    global pt1,pt2,topleft_clicked,bottomright_clicked
    
    if event == cv.EVENT_LBUTTONDOWN :
        print(event,x,y,flags,param)
        print("mouse clicked")

        if topleft_clicked == True and bottomright_clicked == True:
            # reset the variables if rectangle has already been drawn.
            pt1 =(0,0)
            pt2 =(0,0)
            topleft_clicked = False
            bottomright_clicked = False

        if topleft_clicked == False:
            print("top left clicked")
            pt1 =(x,y)
            topleft_clicked = True
        elif bottomright_clicked == False:
            print("bottom clicked")
            pt2 =(x,y)
            bottomright_clicked = True


cv.namedWindow("Test")
cv.setMouseCallback("Test",draw_rectangle)
while (video.isOpened()) :
    # it will read the vedio frame from camera ,ret is boolean True if frame is available 
    ret,frame =video.read()
    
    if ret == True :
        
    
        font = cv.FONT_HERSHEY_SIMPLEX
        video_dim = "Width :" + str(video.get(cv.CAP_PROP_FRAME_WIDTH)) + " Height :" + str(video.get(cv.CAP_PROP_FRAME_HEIGHT)) +" " + current_time
        video_text = cv.putText(frame, video_dim, (300, 700), font, 1, (0,255,0), 1, cv.LINE_AA)          

        # draw rectangle on vedio frame
        
        # rectangle starting point
        x = int(width // 2)# // returns int while / returns float
        y = int(height // 2)

        # rectangle end point
        xx = int(x + width //4)
        yy = int(y + height //4)

        if topleft_clicked :
            cv.circle(video_text,pt1,1,(0,0,255),1)
        
        if topleft_clicked and bottomright_clicked :
            video_rect = cv.rectangle(video_text,pt2,pt1,(0,255,0),4)

        cv.imshow("Test",video_text)

        #for camera value is 1
        key = cv.waitKey(1)

        if key == ord('q'):
            break
    else :
        break

# to release the resources from memory ie camera
cv.setMouseCallback('grat Vedio',draw_rectangle)
video.release()
output.release()
#to destroy all opened windows.
#cv.destroyAllWindow()
