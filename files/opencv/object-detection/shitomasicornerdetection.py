#https://docs.opencv.org/3.4/d4/d8c/tutorial_py_shi_tomasi.html

import cv2 as cv
import numpy as np


shape =cv.imread("files/opencv/object-detection/chess.png")
gray = cv.cvtColor(shape,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,500,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(shape,(x,y),3,(0,0,255),-1)

cv.imshow("result",shape)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()