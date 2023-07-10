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

img =cv.imread("files/opencv/object-detection/desk-office-keyboard-apple.jpeg")
#img =cv.imread("files/opencv/object-detection/geometric-shapes.jpeg")

cv.imshow("original",img)
# BGR 2 GRAY
gray_img =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray image",gray_img)

# noise removal using GaussianBlur
ksize =(3,3)
blur_img = cv.GaussianBlur(gray_img,ksize,0)

# edge detection using canny
edges = cv.Canny(blur_img,threshold1=20,threshold2=100)
cv.imshow("canny edged",edges)



if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
