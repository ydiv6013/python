import cv2 as cv
import numpy as np



img = cv.imread("files/opencv/brick.jpg")

if img is None :
    print("something went wromg!!")
else :
    cvt_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    # blue histogram BGR ,Blue = 0
    bhistogram =cv.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
    print(bhistogram.shape)
    cv.imshow("blue histogram",bhistogram)



cv.waitKey(0)
cv.destroyAllWindows()