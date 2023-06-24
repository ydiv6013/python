import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('files/opencv/dog.jpg')

if img is None :
    print("Opps something went Wrong")

else :
    print(img.shape)
    img_GRAY = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    img_GRAY=cv.resize(img_GRAY,(600,600))
    img_RGB = cv.resize(img_RGB,(450,450))
    img = cv.resize(img,(400,400))
    cv.imshow('images',img_GRAY)
    cv.imshow('images rgb',img_RGB)
    cv.imshow('img',img)

    img_flipped = cv.flip(img,1)
    cv.imshow('flipped images',img_flipped)


key = cv.waitKey(0)

if key == ord('q'):
    cv.imwrite('files/opencv/new-dog.jpg',img_flipped)

cv.destroyAllWindows()  