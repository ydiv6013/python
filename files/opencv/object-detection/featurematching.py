import cv2 as cv
import numpy as np

def BF_matching_ORB():

    #Brute-Force Matching with ORB Descriptors
    #https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

    img =cv.imread("files/opencv/object-detection/reeses.jpeg",0)
    ressesspuff =cv.imread("files/opencv/object-detection/ressespuff3.jpeg",0)
    cv.imshow("image",img)
    cv.imshow("image2",ressesspuff)

    # Initiate ORB detector
    orb = cv.ORB_create()

    # find the keypoints and descriptors with ORB

    kp1, des1 = orb.detectAndCompute(img,None)
    kp2, des2 = orb.detectAndCompute(ressesspuff,None)

    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    print(len(matches))
    # Draw first 10 matches.
    img3 = cv.drawMatches(img,kp1,ressesspuff,kp2,matches[:-1],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow("image3",img3)


def BF_matching_SHIFT():

    #Brute-Force Matching with ORB Descriptors
    #https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

    img =cv.imread("files/opencv/object-detection/reeses.jpeg",0)
    ressesspuff =cv.imread("files/opencv/object-detection/ressespuff1.jpeg",0)
    cv.imshow("image11",img)
    cv.imshow("image21",ressesspuff)

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # find the keypoints and descriptors with SHIFT

    kp1,des1 = sift.detectAndCompute(img,None)
    kp2,des2 = sift.detectAndCompute(ressesspuff,None)

    # BFMatcher with default params
    bf = cv.BFMatcher()
    # Match descriptors.
    matches = bf.knnMatch(des1,des2,k=2)

    # Apply ratio test ,The lower the distance, the better it is.
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    
    # Draw first all matches.
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img,kp1,ressesspuff,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow("image31",img3)


def BF_matching_SHIFT_FLANN():

    #Brute-Force Matching with  SIFT  Descriptors and FLANN based Matcher
    #https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

    img =cv.imread("files/opencv/object-detection/reeses.jpeg",0)
    ressesspuff =cv.imread("files/opencv/object-detection/ressespuff1.jpeg",0)
    cv.imshow("image111",img)
    cv.imshow("image211",ressesspuff)

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # find the keypoints and descriptors with SHIFT

    kp1,des1 = sift.detectAndCompute(img,None)
    kp2,des2 = sift.detectAndCompute(ressesspuff,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50) # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    # Match descriptors.
    matches = flann.knnMatch(des1,des2,k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]

    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = (255,0,0),
                       matchesMask = matchesMask,
                       flags = cv.DrawMatchesFlags_DEFAULT)
    
    # Draw first all matches.
    img3 = cv.drawMatchesKnn(img,kp1,ressesspuff,kp2,matches,None,**draw_params)
    cv.imshow("image311",img3)


BF_matching_ORB()
BF_matching_SHIFT()
BF_matching_SHIFT_FLANN()

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()