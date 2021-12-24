import cv2 as cv

# declaring path
path1=r"videos/OnePunchMan.mp4"

capture1=cv.VideoCapture(path1) # for a video on device
capture2=cv.VideoCapture(0) # for video cam

# reading frame by frame
while(True):

    isTrue, frame=capture1.read()

    # if video ends, frame does not exist, or isTrue is false
    if(isTrue):

        # showing video
        cv.imshow("Test_video_1",frame)

        # termination by presing q
        if((cv.waitKey(25)&0xFF)==ord('q')):
            break

    else:
        break

capture1.release()
cv.destroyAllWindows()

frame_width=int(capture2.get(3))
frame_height=int(capture2.get(4))

# capture2.set(3,int(frame_width*0.5))
# capture2.set(4,int(frame_height*0.5))

output = cv.VideoWriter('Test_video_write.mp4',cv.VideoWriter_fourcc('M','J','P','G'), 24, (frame_width,frame_height)) # or *'MJPG'

# reading frame by frame
while(True):

    isTrue, frame=capture2.read()

    if(isTrue):

        # showing video
        cv.imshow("Test_video_2",frame)

        output.write(frame)

        # termination by presing q
        if((cv.waitKey(25)&0xFF)==ord('q')):
            break
    
    else:
        break

capture2.release()
output.release()
cv.destroyAllWindows()


