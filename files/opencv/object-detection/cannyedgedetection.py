#https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

import cv2 as cv
import numpy as np


img =cv.imread("files/opencv/object-detection/dog.jpg",1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.blur(gray,ksize=(10,10))

edges = cv.Canny(blur,threshold1=30,threshold2=30)
cv.imshow("original",img)
cv.imshow("result",edges)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
