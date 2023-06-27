import cv2 as cv
import numpy as np

def contourdetection():
    img =cv.imread("files/opencv/object-detection/geoshape.jpeg",0)
    cv.imshow("Geometric shapes",img)

    # threshold image
    ret, thresh = cv.threshold(img,thresh=127,maxval=255,type=1)

    # find countours both internal and external
    image, contours= cv.findContours(thresh,cv.RETR_LIST,
                                                 cv.CHAIN_APPROX_SIMPLE)
    
    print(contours)
    print(len(contours))
    img_copy = img.copy()
    cv.drawContours(img_copy, contours,-1, (0,255,0),3)
    cv.imshow("result",img)




contourdetection()

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()