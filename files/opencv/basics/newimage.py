import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image



blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)
cv.imshow('blank image',blank_img)



key = cv.waitKey(0)

cv.destroyAllWindows()  