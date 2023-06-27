import cv2 as cv
import numpy as np

# https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html

chess1 = cv.imread("files/opencv/object-detection/Chess_board.jpeg")
chess2 = cv.imread("files/opencv/object-detection/Chess_Board.png")
shape =cv.imread("files/opencv/object-detection/shape.jpeg")
cv.imshow("chess1",chess1)
cv.imshow("chess2",chess2)

gray1 = cv.cvtColor(chess1,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(chess2,cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(shape,cv.COLOR_BGR2GRAY)
gray1 = np.float32(gray1)
gray2 = np.float32(gray2)
gray3 = np.float32(gray3)

dst = cv.cornerHarris(gray3,blockSize=2,ksize=3,k=0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
shape[dst>0.01*dst.max()]=[0,0,255]

cv.imshow("result",shape)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()