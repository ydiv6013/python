import cv2 as cv

ranbow_img = cv.imread("files/opencv/rainbow.jpg",0)
newspaper_img =cv.imread("files/opencv/newspaper.jpeg",0)


if ranbow_img is None or newspaper_img is None:
    print("Opps something went Wrong")

else :
    ranbow_img = cv.resize(ranbow_img,(600,400))
    cv.imshow("rainbow",ranbow_img)
    print(ranbow_img.shape)
    
    # maxvalue upto 255 
    maxval = ranbow_img.max()

    thresh = int( maxval / 2)
    print(thresh,ranbow_img.max())

    #any value of image rainbow_img below thresh will be shifted to 0 and 
    #any value of image rainbow_img above thresh will be shifted to maxval
    
    ret,thresh1 = cv.threshold(ranbow_img,thresh,maxval,cv.THRESH_BINARY)
    print(ret)
    cv.imshow("Threshhold image",thresh1)
    ret2,thresh2 = cv.threshold(ranbow_img,thresh,maxval,cv.THRESH_BINARY_INV)
    print(ret2)
    cv.imshow("Threshhold image2",thresh2)

    ret3,thresh3 = cv.threshold(ranbow_img,thresh,maxval,cv.THRESH_TRUNC)
    print(ret3)
    cv.imshow("Threshhold image3",thresh3)



    # newspaper

    # maxvalue upto 255 
    maxval = ranbow_img.max()

    thresh = int( maxval / 2)
    print(thresh,newspaper_img.max())

    #any value of image rainbow_img below thresh will be shifted to 0 and 
    #any value of image rainbow_img above thresh will be shifted to maxval
    
    nret,nthresh1 = cv.threshold(newspaper_img,200,maxval,cv.THRESH_BINARY)
    print(nret)
    cv.imshow("Newspaper image",nthresh1)
    nret2,nthresh2 = cv.threshold(newspaper_img,200,maxval,cv.THRESH_BINARY_INV)
    print(nret2)
    cv.imshow("Newspaper  image2",nthresh2)

    nret3,nthresh3 = cv.threshold(newspaper_img,220,maxval,cv.THRESH_TRUNC)
    print(nret3)
    cv.imshow("Newspaper  image3",nthresh3)





# adaptive threshold

adaptive_thresh = cv.adaptiveThreshold(newspaper_img,255,
                                       cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY,11,5)
cv.imshow("adaptive threshold",adaptive_thresh)
cv.waitKey(0)
cv.destroyAllWindows()
