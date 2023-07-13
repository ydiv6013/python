#importing the opencv module  
import cv2 as cv
import sys
import numpy as np
## [imports]

## [imread]
# using imread('path') and 0 = grayscale image & 1 as rgb (default),-1 as unchanged ,its optional
#Flags

#cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
#cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
img = cv.imread("files/opencv/cocacola.png")
## [imread]
## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]

#convert BGR image to Gray or RGB
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# convert BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#This is using for display the image  
cv.imshow("Images coca", rgb)



## [imsave]

#print the pixel value at pixel position 150,800
pixel = img[150,600]
print(pixel)


# height, width, number of channels in image  
dimensions = img.shape
height = img.shape[0]  
width = img.shape[1]  


# print data-type of image
print("Data type of image is:", img.dtype)

try :
    channels = img.shape[2]  
except:
    img = cv.imread('files/opencv/logo.png',1)
    
size1 = img.size  
  
print('Image Dimension(H, W, C) is : ',dimensions)  
print('Image Height(H)      : ',height)  
print('Image Width(W)       : ',width)  
print('Number of Channels(C): ',channels)  
print('Image size is.       : ', size1)  


# split image 

b,g,r = cv.split(img)

# cv2.split() function is a slow function. Numpy indexing is quit efficient and it should be used if possible.
#g = img[:,0,:]
#b = img[:,:,0]
#r = img[0,:,:]
#print(b,g,r)


#merge image
img2=cv.merge((b,g,r))
#It will run continuously until the key press.  


#modifying image pixel

copy_img = img.copy()

copy_img[150,600] =200
copy_img[151,601]=200
copy_img[152,602]=200
copy_img[153,600] =200
copy_img[154,601]=200
copy_img[155,602]=200
copy_img[156,600] =200
copy_img[157,601]=200
copy_img[158,602]=200
copy_img[159,600] =200
copy_img[161,601]=200
copy_img[162,602]=200
copy_img[160,600] =200
copy_img[163,601]=200
copy_img[164,602]=200

k = cv.waitKey(0)
## [imshow]
## [imsave]


# image manipulation 
#draw line image object,staring point and ending point,color in bgr ,thickness

newimage = cv.line(img,(100,100),(600.600),(255,0,0) ,5) 

cv.imshow('line image',newimage)

if k == ord("s"):
    cv.imwrite("files/opencv/starry_night.jpg",copy_img)

cv.destroyAllWindows()  

