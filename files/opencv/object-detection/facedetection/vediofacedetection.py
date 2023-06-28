#importing the opencv module  
import cv2 as cv
import numpy as np

# it will run the camera 
video = cv.VideoCapture(0)
# status of file or vedio it wil return True or False
print(video.isOpened())

def detect_face(img):
    face_img = img.copy()
    # harcascade frontalface
    face_cascade = cv.CascadeClassifier("files/opencv/object-detection/facedetection/data/haarcascades/haarcascade_frontalface_default.xml")
    face_rectangle = face_cascade.detectMultiScale(face_img,scaleFactor =1.2,minNeighbors=6)
    print("face_rectangle :" ,face_rectangle)
    for (x,y,width,height) in face_rectangle :
        cv.rectangle(face_img,(x,y),(x+width,y+height),color=(255,255,255),thickness=5)
    return face_img


while (video.isOpened()) :
    # it will read the vedio frame from camera ,ret is boolean True if frame is available 
    ret,frame =video.read(0)
    
    if ret == True :
        frame = detect_face(frame)
        cv.imshow("face detection",frame)
        #for camera value is 1
        key = cv.waitKey(1) & 0xFF

        if key == ord('q'):
            break

# to release the resources from memory ie camera
video.release()
