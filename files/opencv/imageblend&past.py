import cv2 as cv

img1 = cv.imread("files/opencv/dog.jpg")
img2 =cv.imread("files/opencv/logo.png")

if img1 is None  or img2 is None:
    print("Opps something went Wrong")

else :
    print(img1.shape)
    print(img2.shape)
    img1 =cv.resize(img1,(1000,900))
    img2 = cv.resize(img2,(1000,900))
    print(img1.shape,img2.shape)
    cv.imshow("Dog image",img1)
    cv.imshow("Dog HSV",img2)
    # addWeighted works only with same size images
    blended = cv.addWeighted(img1,0.5,img2,0.5,0)
    cv.imshow("image Blended",blended)


key = cv.waitKey(0)
cv.destroyAllWindows()