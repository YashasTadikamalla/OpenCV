import cv2 as cv

path=r"videos/OnePunchMan.mp4"

capture=cv.VideoCapture(path)
i=0
no=0

while(True):
    isTrue, frame=capture.read()

    if(isTrue):
        if(no%5==0):
            cv.imwrite("yt_manali_"+str(i)+".jpg", frame)
            i+=1
    
    else:
        break

    no+=1

capture.release()