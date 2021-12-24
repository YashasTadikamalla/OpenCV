import cv2 as cv
import numpy as np

path=r'images/AOT.jpg'

img=cv.imread(path)
cv.imshow('AOT',img)
cv.waitKey(0)

# import matplotlib.pyplot as plt 

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('AOTgray',gray_img)
cv.waitKey(0)
cv.destroyAllWindows()

h,w=gray_img.shape[:2]

blank=np.zeros((h,w),dtype='uint8')
circle=cv.circle(blank,(w//2,h//2),h//4,255,-1)
cv.imshow('filter',circle)
cv.waitKey(0)
cv.destroyAllWindows()

mask=cv.bitwise_and(gray_img,circle)
cv.imshow('filtered',mask)
cv.waitKey(0)
cv.destroyAllWindows()


# histo_mask=cv.calcHist([gray_img],[0],mask,[256],[0,255])
# plt.plot(histo_mask)
# plt.xlim([0,255])
# plt.show()

# histo=cv.calcHist([gray_img],[0],None,[256],[0,255])
# plt.plot(histo)
# plt.xlim([0,255])
# plt.show()

threshold_val, thresh_img=cv.threshold(gray_img,120,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh_img)
cv.waitKey(0)

ada_thresh_img=cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,0)
cv.imshow('ada_thresh',ada_thresh_img)
cv.waitKey(0)

# adaptive thresh


