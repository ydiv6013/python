# Edge and Contour Detection
import cv2 as cv
import numpy as np

img =cv.imread("files/opencv/object-detection/geo-shapes.jpeg")
cv.imshow("Geometric shapes",img)

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blur image
img_blur= cv.GaussianBlur(gray_img,ksize=(3,3),sigmaX=0)

# threshold image
ret, thresh = cv.threshold(img_blur,thresh=127,maxval=255,type=1)
cv.imshow("thresh",thresh)

# find countours both internal and external
contours,hierarchy= cv.findContours(thresh,cv.RETR_EXTERNAL,
                                                 cv.CHAIN_APPROX_SIMPLE)

print(len(contours))
img_copy = img.copy()
cv.drawContours(img_copy,contours,-1,(0,0,255),3)
cv.imshow("result",img_copy)


if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()