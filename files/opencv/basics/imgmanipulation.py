import cv2 as cv
import sys
import numpy as np

img =cv.imread('files/opencv/adhar.png',1)

#img = np.zeros([512, 512, 3], np.uint8)

if img is None:
    sys.exit("Could not read the image.")
## [empty]

# image manipulation 
#draw line image object,staring point and ending point,color in bgr ,thickness

img = cv.line(img,(100,100),(600,600),(255,0,0), 5) 
img = cv.line(img, (180,150), (180,600), (147, 96, 44), 10) # 44, 96, 147

img = cv.arrowedLine(img, (0,255), (200,200), (255, 100, 80), 10)
img =cv.rectangle(img,(200,300),(450,350),(0,0,255),2)
#filled rectangle thickness = -1
img =cv.rectangle(img,(500,300),(450,350),(0,255,0),-1)

img =cv.circle(img,(155,255),55,(255,0,0),-1)
img =cv.circle(img,(505,255),55,(0,250,0),2)

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, 'Adharcard', (100, 500), font, 3, (0,0, 255), 5, cv.LINE_AA)

img = cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv.polylines(img,[pts],True,(255,0,255),5)

cv.imshow('line image',img)

key = cv.waitKey(0)
if key == ord("s"):
    cv.imwrite("files/opencv/aadhar-new.jpg",img)

cv.destroyAllWindows()  