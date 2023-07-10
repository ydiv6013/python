import cv2 as cv
import numpy as np


nadia = cv.imread("files/opencv/object-detection/facedetection/Nadia_Murad.jpeg",1)
denis = cv.imread("files/opencv/object-detection/facedetection/denis-mukwege.jpeg",1)
solway = cv.imread("files/opencv/object-detection/facedetection/solway-conference.jpeg",1)
actors =cv.imread("files/opencv/object-detection/facedetection/actors.jpeg",1)
avengers =cv.imread("files/opencv/object-detection/facedetection/avengers.jpeg",1)

def detect_eye(img):
    eye_img = img.copy()
    # harcascade frontaleye
    eye_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_eye.xml")
    eye_rectangle = eye_cascade.detectMultiScale(eye_img)

    for (x,y,width,height) in eye_rectangle :
        cv.rectangle(eye_img,(x,y),(x+width,y+height),color=(0,0,255),thickness=5)
    
    return eye_img

def improved_detect_eye(img):
    eye_img = img.copy()
     # harcascade frontaleye
    eye_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_eye.xml")
    eye_rectangle = eye_cascade.detectMultiScale(eye_img,scaleFactor=1.2,minNeighbors=6)

    for (x,y,width,height) in eye_rectangle :
        cv.rectangle(eye_img,(x,y),(x+width,y+height),color=(0,0,255),thickness=5)
    
    return eye_img
    
result =detect_eye(actors)
cv.imshow("result",result)
improved_result = improved_detect_eye(actors)
cv.imshow("improved result",improved_result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()