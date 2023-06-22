import cv2 as cv
import numpy as np

brick = cv.imread("files/opencv/brick.jpg")
noise_img = cv.imread("files/opencv/balloons_noisy.png")



if brick is None or noise_img is None:
    print("Opps something went Wrong")
else :
    print(brick.shape)
    brick = cv.resize(brick,(1200,700))
    print(brick.shape)
    cv.imshow("brick",brick)

    brick = cv.putText(brick,"Bricks",(100,100),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),7)

    # gamma correction  or blurring

    kernel = np.ones((5,5),dtype=np.float32) / 25
    destination = cv.filter2D(brick,-1,kernel)
    cv.imshow("gamama",destination)

    print(kernel)

    # using .blur method 
    blurred = cv.blur(brick,ksize=(9,9))
    cv.imshow("blurred image",blurred)

    #using GaussianBlur
    blurred_gc = cv.GaussianBlur(brick,ksize=(5,5),sigmaX=10)
    cv.imshow("gussian blurr",blurred_gc)

    #using medianBlur
    median_blur = cv.medianBlur(brick,3)
    cv.imshow("median blurr",median_blur)

    # remove noise using medianBlur
    cv.imshow("noisy image",noise_img)
    noise = cv.medianBlur(noise_img,ksize=7)
    cv.imshow("removed noise",noise)

    bl =cv.bilateralFilter(brick,5,10,10)
    cv.imshow("bilateral" , bl)


cv.waitKey(0)
cv.destroyAllWindows()