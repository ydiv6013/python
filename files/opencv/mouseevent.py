import cv2 as cv

#dir is a inbuilt functions that returens list of events
events = [events for events in dir(cv)]

print(events)

#dir is a inbuilt functions that returens list of mouse  events
mouse_events = [events for events in dir(cv) if 'EVENT' in events]

print(mouse_events)

img = cv.imread("files/opencv/cocacola.png")
cv.imshow('image',img)
def mouse_click(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN :
        pos = 'LCLICK'+'('+str(x) +','+ str(y) + ')'
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, pos, (x,y), font, 
                         0.5, (105,200,0), 2, cv.LINE_AA)
        cv.imshow('image',img)

    if event == cv.EVENT_RBUTTONDOWN :

        blue =img[y,x,0]
        green =img[y,x,1]
        red =img[y,x,2]

        strBGR= 'RCLICK'+'('+str(blue) +','+ str(green) +','+ str(red) +')'
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, strBGR, (x,y), font, 
                         0.5, (0,200,250), 2, cv.LINE_AA)
        cv.imshow('image',img)


# below method calls the mouse_click function.
cv.setMouseCallback('image',mouse_click)
key =cv.waitKey(0)
cv.destroyAllWindows()