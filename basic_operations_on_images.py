import cv2 as cv
import numpy as np

# declaring paths
path1=r"DeathNote.jpg"
path2=r"images/DeathNote.jpg"

# reading them
# default flag is for color image - cv.IMREAD_COLOR or 1
image1=cv.imread(path1,cv.IMREAD_GRAYSCALE) # np 2D array 
image2=cv.imread(path2) # np 3D array (np 2D array of list of size 3 (i.e, [r,b,g]))

# capturing size: height and width in h, w
h,w=image1.shape[:2]
B,G,R=image2[150,250]

# showing them
cv.imshow("Test_pic_1",image1)
cv.waitKey(3000) # waits for 3000ms and then moves to next, if not interrupted by keyboard 
cv.destroyAllWindows()
cv.imshow("Test_pic_2",image2)
cv.waitKey(0) # waits untill keyboard interrupt for infinite time, before moving to next
cv.destroyAllWindows()

# blank image, shapes on images
blank=np.ones((200,200),dtype='uint8')*125
cv.imshow('blank',blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank=np.ones((200,200,3),dtype='uint8')*125
cv.imshow('blank',blank)
cv.waitKey(0)
blank=np.ones((200,200,3),dtype='uint8')*125
blank[50:100,100:150]=[245,57,89]
cv.imshow('blank',blank)
cv.waitKey(0)
cv.destroyAllWindows()

print(f'height is: {h},\nwidth is: {w}')
print(f'B,G,R for pixel (150,250) of image2 are {B},{G},{R}') # point on apple

# extracting apple from image2
red_apple=image2[70:193,193:315]

# resizing image
large_red_apple=cv.resize(red_apple,(500,500))

# rotating image
rotmat=cv.getRotationMatrix2D((w//2,h//2),60,1)
new_image=cv.warpAffine(image1,rotmat,(w,h))

cv.imshow('apple_extracted',red_apple)
cv.waitKey(2000)
cv.imshow('apple_enlarged',large_red_apple)
cv.waitKey(0)
cv.imshow('tilted_image1',new_image)
cv.waitKey(0)
cv.destroyAllWindows()

img1=image1.copy()

# drawing rectangle on image (permanent edit)
edit1=cv.rectangle(img1,(193,70),(315,193),(230,230),2)
cv.imshow('apple in box',img1) # or edit1
cv.waitKey(0)

edit1=cv.rectangle(img1,(193,70),(315,193),(230,230),cv.FILLED)
cv.imshow('apple in box',img1) # or edit1
cv.waitKey(0)
cv.destroyAllWindows()

# writing on image
edit2=cv.putText(image2,'Ryuk',(193,150),cv.FONT_HERSHEY_PLAIN,3,(230,110,30),1)
edit3=cv.circle(image2,(255,130),75,(23,45,89),2)
edit4=cv.line(image2,(20,30),(140,150),(40,150,40),2)
cv.imshow('text on apple',image2) # or edit2
cv.waitKey(0)
cv.destroyAllWindows()

# creating new image
cv.imwrite("editedDeathNote.jpg",img1)

# drawing line




