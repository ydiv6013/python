#https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

import cv2 as cv
import numpy as np

"""
The Canny edge detector algorithm has four steps:

    1.Noise reduction by blurring the image using a Gaussian blur.
    2.Computing the intensity gradients of the image.
    3.Suppression of Edges.
    4.Using hysteresis thresholding.
"""

video = cv.VideoCapture(0)

while (video.isOpened()):

    # reads frames from a camera
    ret ,frame = video.read()

    # converting BGR to HSV
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # noise removal using GaussianBlur
    ksize =(3,3)
    blur_img = cv.GaussianBlur(gray_frame,ksize,0)

    # edge detection using canny
    edges = cv.Canny(blur_img,threshold1=100,threshold2=200)
    cv.imshow("canny edged",edges)

    # find a contour 
    contours,hierarchy = cv.findContours(edges,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    print("contours found",len(contours))
    print(contours)


    #draw contour
    img_copy = frame.copy()
    cv.drawContours(img_copy,contours,-1,(0,0,255),5)
    cv.imshow("original frame",frame)
    cv.imshow("contours",img_copy)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()