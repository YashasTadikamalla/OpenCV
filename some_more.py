import cv2 as cv
import numpy as np

img=cv.imread('images/SteinsGate.png',0)
cv.imshow('pic',img)
cv.waitKey(0)

# edge detection using Laplacian- look like drawn on a chalkboard
lap_ed=cv.Laplacian(img,cv.CV_64F)
lap=np.uint8(np.absolute(lap_ed))
cv.imshow('edge_lap',lap)
cv.waitKey(0)

# canny edges- look like computer generated- its more advanced 
cann_ed=cv.Canny(img,100,200)
cv.imshow('edge_canny',cann_ed)
cv.waitKey(0)

# edge detection using sobel- uses gradients to find edges
sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)
sobel_overall=cv.bitwise_or(sobelx,sobely)

cv.imshow('sx',sobelx)
cv.waitKey(0) 
cv.imshow('sy',sobely)
cv.waitKey(0)
cv.imshow('final_sobel',sobel_overall)
cv.waitKey(0)