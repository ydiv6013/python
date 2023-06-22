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


# image blending of smaller size over big size image.
    
    img2 = cv.resize(img2,(300,200))
    cv.imshow("resized logo",img2)
    print(img2.shape)

    

    # roi = region of interest for img2
    x_start = 0
    y_start = 0
    x_end= x_start + img2.shape[0]
    y_end = y_start + img2.shape[1]

    roi = img2[x_start : x_end,y_start : y_end]
    cv.imshow("masked image",roi)
    print(roi.shape)


    large_image = img1
    small_image = roi
    print("small image shape : " , small_image.shape)

    large_image[y_start:y_start+small_image.shape[0]
                 ,x_start : x_start + small_image.shape[1]] = small_image
    
    cv.imshow("merged image",large_image)

key = cv.waitKey(0)
cv.destroyAllWindows()