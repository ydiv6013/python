import cv2 as cv
import numpy as np
import math


blank_img = np.zeros((600,600))
font =cv.FONT_HERSHEY_COMPLEX
blank_img = cv.putText(blank_img,"YOGESH",(100,100),fontFace=font,fontScale=3,color=(255,255,255),thickness=7)

cv.imshow("image",blank_img)


# mporphological operators

# erode

kernel = np.ones((5,5),dtype=np.int8)
print(kernel)

erode = cv.erode(blank_img,kernel=kernel,iterations=2)
cv.imshow("eroded",erode)

# white noise
white_noise = np.random.randint(low=0,high=2,size=(600,600),dtype=np.uint8)
white_noise =white_noise *255

cv.imshow("white noise",white_noise)

noise_img = white_noise + blank_img

cv.imshow("noise image",noise_img)

# remove noise using opening 
opening = cv.morphologyEx(blank_img,cv.MORPH_OPEN,kernel=kernel)

cv.imshow("opening" ,opening)
#remove nooise using closing

# remove noise using opening 
closing = cv.morphologyEx(blank_img,cv.MORPH_CLOSE,kernel=kernel)

cv.imshow("closing" ,closing)

# remove noise using gradient
gradient = cv.morphologyEx(blank_img,cv.MORPH_GRADIENT,kernel=kernel)

cv.imshow("gradient" ,gradient)

cv.waitKey(0)
cv.destroyAllWindows()