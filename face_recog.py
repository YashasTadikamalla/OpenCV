import cv2 as cv
import numpy as np
import os

face_cascade=cv.CascadeClassifier('haar_cascade_face.xml')

cwd=os.getcwd()
dir_name=r'actors_train'
path_train=os.path.join(cwd,dir_name)

face_cascade=cv.CascadeClassifier('haar_cascade_face.xml')

actors=[]

for dir in os.listdir(path_train):
    actors.append(dir)

# images=np.load('images_of_faces_only.npy')
# labels=np.load('labels.npy')

face_recog=cv.face.LBPHFaceRecognizer_create()
face_recog.read('trained.yml')

test_path=r'actors_test/CE/images (2).jpeg'
test_img=cv.imread(test_path,0)

cv.imshow('test',test_img)
cv.waitKey(0)

rect_coords=face_cascade.detectMultiScale(test_img,1.2,5)

for (x,y,w,h) in rect_coords:
    roi=test_img[y:y+h,x:x+w]

    label, confidence= face_recog.predict(roi)

    cv.putText(test_img,str(actors[label]),(20,20),cv.FONT_HERSHEY_PLAIN,2,(0,233,56),2)
    cv.rectangle(test_img,(x,y),(x+w,y+h),(0,233,56),2)

cv.imshow('test',test_img)
cv.waitKey(0)