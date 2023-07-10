import cv2 as cv
import numpy as np


img = cv.imread("files/opencv/object-detection/dog.jpg")
face = cv.imread("files/opencv/object-detection/face-dog.jpg")
imgcp = img.copy()
w = face.shape[0]
h = face.shape[1]

print(w,h)

if img is None or face is None :
    print("Opps something went wrong")
else :
    cv.imshow("image",img)
    cv.imshow("face",face)

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for m in methods :
    img = imgcp.copy()
    method = eval(m)
    print(f" method is {method,type(method)},m is {m}")

    # Apply template Matching
    result = cv.matchTemplate(img,face,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("dimension : " , cv.minMaxLoc(result))
    print(min_val, max_val, min_loc, max_loc)

     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        print(top_left)
        bottom_right = (top_left[0]+w,top_left[1]+ h)
        print(bottom_right)
        
    rectangle = cv.rectangle(img,top_left,bottom_right,(255,0,0),4)
    text = m
    font = cv.FONT_HERSHEY_SIMPLEX
    puttext = cv.putText(img, text, (100, 500), font, 3, (0,0, 255), 5, cv.LINE_AA)
    cv.imshow("rectangle",puttext)
       
   
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()