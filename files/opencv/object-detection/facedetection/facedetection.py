import cv2 as cv
import numpy as np


nadia = cv.imread("files/opencv/object-detection/facedetection/Nadia_Murad.jpeg",1)
denis = cv.imread("files/opencv/object-detection/facedetection/denis-mukwege.jpeg",1)
solway = cv.imread("files/opencv/object-detection/facedetection/solway-conference.jpeg",1)
actors =cv.imread("files/opencv/object-detection/facedetection/actors.jpeg",1)
avengers =cv.imread("files/opencv/object-detection/facedetection/avengers.jpeg",1)


cv.imshow("nadia",nadia)
cv.imshow("denis",denis)
cv.imshow("solway",solway)

def detect_face(img):
    face_img = img.copy()
    # harcascade frontalface
    face_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_frontalface_default.xml")
    face_rectangle = face_cascade.detectMultiScale(face_img)
    print(face_rectangle)

    for (x,y,width,height) in face_rectangle :
        cv.rectangle(face_img,(x,y),(x+width,y+height),color=(0,0,255),thickness=5)
    
    return face_img

def improved_detect_face(img):
    face_img = img.copy()
     # harcascade frontalface
    face_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_frontalface_default.xml")
    face_rectangle = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=6)

    for (x,y,width,height) in face_rectangle :
        cv.rectangle(face_img,(x,y),(x+width,y+height),color=(0,0,255),thickness=5)
    
    return face_img
    
result =detect_face(solway)
cv.imshow("result",result)
improved_result = improved_detect_face(solway)
cv.imshow("improved result",improved_result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()