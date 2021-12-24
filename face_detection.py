import cv2 as cv
import numpy as np

path1=r'images/AOT.jpg'
path2=r'images/SteinsGate.png'

img1=cv.imread(path1,0)
img2=cv.imread(path2,0)

im1=img1.copy()
im2=img2.copy()

face_cascade=cv.CascadeClassifier(r'haar_cascade_face.xml')
# rect_coords=face_cascade.detectMultiScale(img1,1.2,3)
rect_coords=face_cascade.detectMultiScale(img2,1.2,3)

print(f'Number of faces found {len(rect_coords)}')
# print(f'{img1.shape[:2]}')
for (x,y,w,h) in rect_coords:
    # cv.rectangle(im1,(x,y),(x+w,y+h),(20,40,260),2)
    cv.rectangle(im2,(x,y),(x+w,y+h),(20,40,260),2)

# cv.imshow('faces',im1)
cv.imshow('faces',im2)
cv.waitKey(0)

