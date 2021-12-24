import numpy as np
import cv2 as cv

img1=cv.imread('images/SteinsGate.png')
img2=cv.imread('images/AOT.jpg')

cv.imshow('Steins;Gate',img1)
cv.waitKey(0)
cv.imshow('AOT',img2)
cv.waitKey(0)

cv.destroyAllWindows()

# BGR to gray
gray_img1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray_img1)
cv.waitKey(0)

# blur
blur_img1=cv.GaussianBlur(img1,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur_img1)
cv.waitKey(0)
cv.imshow('Steins;Gate',img1)
cv.waitKey(0)

cv.destroyAllWindows()

# add images of same size
wt_sum=cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow('added',wt_sum)
cv.waitKey(0)

# subtract images of same size
sub=cv.subtract(img1,img2)
cv.imshow('subtracted',sub)
cv.waitKey(0)

cv.destroyAllWindows()

# similarly we can do bitwise oerations like and, or, xor, not on images of same sizes

# erosion 
er_img2=cv.erode(img2,(5,5),iterations=5)
cv.imshow('AOT',img2)
cv.waitKey(0)
cv.imshow('eroded',er_img2)
cv.waitKey(0)
# edge dilation 
dil_img2=cv.dilate(er_img2,(5,5),iterations=5)
cv.imshow('dilated',dil_img2)
cv.waitKey(0)

cv.destroyAllWindows()

# edge detection
edge_img2=cv.Canny(img2,100,200)
cv.imshow('edges',edge_img2)
cv.waitKey(0)
er_edge_img2=cv.Canny(er_img2,100,200)
cv.imshow('er_edges',er_edge_img2)
cv.waitKey(0)
dil_edge_img2=cv.Canny(dil_img2,100,200)
cv.imshow('dil_edges',dil_edge_img2)
cv.waitKey(0)



cv.destroyAllWindows()
