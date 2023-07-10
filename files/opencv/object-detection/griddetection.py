import cv2 as cv
import numpy as np

def chessgrid():
    img =cv.imread("files/opencv/object-detection/Chess_Board.png")

    # find chessbord corners
    chess_grid_size=(7,7)
    found,corners = cv.findChessboardCorners(img,patternSize=chess_grid_size)
    print(cv.findChessboardCorners(img,patternSize=chess_grid_size))
    print(found,corners)

    # draw chessboard corners
    img_copy = img.copy()
    img_copy=cv.drawChessboardCorners(img_copy,patternSize=chess_grid_size,corners=corners,
                                      patternWasFound=found)
    cv.imshow("draw grid",img_copy)
    cv.imshow("original chessboard",img)


def dotgrid():
    img =cv.imread("files/opencv/object-detection/dot-grid.png")
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    # find dotgrid corners
    grid_size=(10,10)
    found,corners = cv.findCirclesGrid(gray,patternSize=grid_size,flags=cv.CALIB_CB_SYMMETRIC_GRID)
    print(cv.findCirclesGrid(gray,patternSize=grid_size,flags=cv.CALIB_CB_SYMMETRIC_GRID))
    print(found,corners)

    # draw chessboard corners
    img_copy = img.copy()
    img_copy=cv.drawChessboardCorners(img_copy,patternSize=grid_size,corners=corners,
                                      patternWasFound=found)
    cv.imshow("draw dot grid ",img_copy)
    cv.imshow("original dotgrid",img)




chessgrid()
dotgrid()



if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()