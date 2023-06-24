import cv2 as cv
import numpy as np


img = cv.imread("files/opencv/sudoku.jpeg",0)

if img is None :
    print("something went wromg!!")
else :
    # here dx=1
   
    sobelx = cv.Sobel(img,ddepth=cv.CV_64F,dx=1,dy=0,ksize=5)
    cv.imshow("soblex",sobelx)

    # here dy=1
   
    sobely = cv.Sobel(img,ddepth=cv.CV_64F,dx=0,dy=1,ksize=5)
    cv.imshow("sobely",sobely)

    #laplacian gradient

    laplacian = cv.Laplacian(img,ddepth=cv.CV_64F)
    cv.imshow("laplacian",laplacian)

    #blending

    blended = cv.addWeighted(src1=sobelx,alpha=0.5,src2=laplacian,beta=0.5,gamma=0)
    cv.imshow("blended",blended)
    # threshold

    ret,threshold = cv.threshold(blended,100,255,cv.THRESH_BINARY)
    cv.imshow("threshold",threshold)

    #gradient using mprph 
    kernel = np.ones((4,4),np.uint8)
    gradient = cv.morphologyEx(threshold,cv.MORPH_GRADIENT,kernel)

    cv.imshow("gradient",gradient)



cv.waitKey(0)
cv.destroyAllWindows()