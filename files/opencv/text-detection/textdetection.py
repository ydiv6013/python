# Import required packages
import cv2 as cv
import sys
import pytesseract as pyt


# Read image from which text needs to be extracted
img = cv.imread("files/opencv/text-detection/data5.jpeg")

if img is None :
    sys.exit("Could not read the image.")
# Preprocessing the image starts

# process to start extra noises
# 1.gray
# 2. bluring image using medianBur (optional)
# 3. image threshold to convert image to balack and white

# 1. Convert the image to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# 2. Blur image using medianBlue

blur_img = cv.medianBlur(gray,ksize=3)
cv.imshow("blur",blur_img)

# Performing OTSU threshold
ret, thresh = cv.threshold(gray, 20, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
cv.imshow("threshold",thresh)

# Creating a copy of image
img2 = thresh.copy()

# find a contour 
contours,hierarchy = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print("contours found",len(contours))

#draw contour
img_copy = img.copy()
cv.drawContours(img_copy,contours,-1,(0,0,255),2)
cv.imshow("contours",img_copy)


# use pytesseract to extract text from images
text = pyt.image_to_string(img2)
text2 = pyt.image_to_boxes(img2)


key = cv.waitKey(0) & 0xFF
if key == ord('q'):
    print("works : \n",text)
    print("text2 : \n",text2)
    with open("files/opencv/text-detection/data.txt","+a") as fh :
        fh.write(text)



cv.destroyAllWindows()