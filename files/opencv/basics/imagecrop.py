import cv2 as cv
import numpy as np


img = cv.imread("files/opencv/basics/dog.jpg")

shape = img.shape
print(shape)
cv.imshow("image",img)

# [rows, columns]
crop = img[280:600, 420:750]  
cv.imshow("croped",crop)


if cv.waitKey(0) & 0xFF == ord('s'):
    cv.imwrite('files/opencv/basics/face-dog.jpg',crop)


cv.destroyAllWindows()