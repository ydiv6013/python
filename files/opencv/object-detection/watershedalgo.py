import cv2 as cv
import numpy as np

def watershed():

    #Brute-Force Matching with ORB Descriptors
    #https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

    img =cv.imread("files/opencv/object-detection/water_coins.jpeg")
    # gray
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # blur image 
    blur = cv.medianBlur(gray,ksize=3)
    # threshold
    ret,thresh =cv.threshold(blur,thresh=160,maxval=255,
                             type=cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh,op=cv.MORPH_OPEN,kernel=kernel,iterations=2)
    
    # sure background area
    sure_bg = cv.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)


    # Marker labelling
    ret, markers = cv.connectedComponents(image=sure_bg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    unknown = 255
    markers[unknown==255] = 0
    markers = cv.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    cv.imshow("image",img)





watershed()

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()