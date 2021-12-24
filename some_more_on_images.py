import cv2 as cv
import numpy as np

path=r'images/AOT.jpg'

img=cv.imread(path)
cv.imshow('AOT',img)
cv.waitKey(0)

# image translation and rotation can be done using cv.warpAffine(). It takes a affine matrix.
# for translation the matrix is [[1 0 x],[0 1 y]], where x is translation to right, y is translation to down
# for rotation, the matrix is given by cv.getRotationMatrix2D, by specifying angle, rotation point and scale factor

# translation

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
def translate(image,x, y):
    h,w=image.shape[:2]

    transMat=np.array([[1,0,x],[0,1,y]],dtype=float)
    new_img=cv.warpAffine(image,transMat,(w,h)) # cv.warpAffine(image,transMat,(w+100,h+200))

    cv.imshow('translated',new_img)
    cv.waitKey(0)

# rotate
def rotate(image, angle, pt=None):
    h,w=image.shape[:2]

    if(pt==None):
        pt=(w//2,h//2)

    rotMat=cv.getRotationMatrix2D(pt,angle,2)
    new_img=cv.warpAffine(image,rotMat,(w+100,h+200))

    cv.imshow('rotated',new_img)
    cv.waitKey(0)

translate(img, 50,100)
rotate(img,45)

flip_img=cv.flip(img,1)
cv.imshow('fliped',flip_img)
cv.waitKey(0)

cv.destroyAllWindows()

# thresholding converts gray scale image to binary
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray_img)
cv.waitKey(0)

ret, th_img=cv.threshold(gray_img,125,255,cv.THRESH_BINARY)
cv.imshow('binary',th_img)
cv.waitKey(0)

cv.destroyAllWindows()