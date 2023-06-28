import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
ret, frame1 = cap.read()

previousimg= cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
hsv_mask = np.zeros_like(frame1)
hsv_mask[:,:,1] = 255
print(hsv_mask)

while True:
    ret, frame2 = cap.read()
    nextimg = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(previousimg, nextimg, None, 
                                       0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv.cartToPolar(flow[:,:, 0], flow[:,:, 1],angleInDegrees=True)
    hsv_mask[:,:,0] = angle/2
    hsv_mask[:,:,2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv_mask, cv.COLOR_HSV2BGR)
    cv.imshow('frame ', bgr)

    
    k = cv.waitKey(10) & 0xff
    if k == ord('q'):
        break

    previousimg = nextimg

cap.release()
cv.destroyWindow()