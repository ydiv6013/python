#importing the opencv module  
import cv2 as cv
import sys
## [imports]

## [imread]
# using imread('path') and 0 = grayscale image & 1 as rgb (default),-1 as unchanged ,its optional
#Flags

#cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
#cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
img = cv.imread("files/opencv/logo.png")
## [imread]
## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]

#This is using for display the image  
cv.imshow("Images", img)

k = cv.waitKey(0)
## [imshow]
## [imsave]

if k == ord("s"):
    cv.imwrite("files/opencv/starry_night.jpg",img)
## [imsave]

#print the pixel value at pixel position 150,800
pixel = img[150,800]
print(pixel)


# height, width, number of channels in image  
dimensions = img.shape
height = img.shape[0]  
width = img.shape[1]  
try :
    channels = img.shape[2]  
except:
    img = cv.imread('files/opencv/logo.png',1)
    
size1 = img.size  
  
print('Image Dimension    : ',dimensions)  
print('Image Height       : ',height)  
print('Image Width        : ',width)  
print('Number of Channels : ',channels)  
print('Image Size  :', size1)  


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
cv.destroyAllWindows()  

