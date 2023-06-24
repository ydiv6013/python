import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("files/opencv/dog.jpg")

print(img)

if img is None :
    print("Opps something went Wrong")

else :
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img,cv.COLOR_RGB2HSV)
    img3 = cv.cvtColor(img,cv.COLOR_RGB2HLS)
    cv.imshow("Dog image",img)
    cv.imshow("Dog HSV",img2)
    cv.imshow("dog HSL",img3)


key = cv.waitKey(0)
cv.destroyAllWindows()