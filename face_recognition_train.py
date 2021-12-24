import os
import cv2 as cv
import numpy as np

cwd=os.getcwd()
dir_name=r'actors_train'
path_train=os.path.join(cwd,dir_name)

face_cascade=cv.CascadeClassifier(r'haar_cascade_face.xml')

actors=[]

for dir in os.listdir(path_train):
    actors.append(dir)

print(actors)

images=[]
labels=[]

def train():
    for actor in actors:
        path_ac=os.path.join(path_train,actor)
        label=actors.index(actor)

        for img in os.listdir(path_ac):
            path_img=os.path.join(path_ac,img)

            im=cv.imread(path_img,0)
            rect_coords=face_cascade.detectMultiScale(im,1.2,5)

            for (x,y,w,h) in rect_coords:
                images.append(im[y:y+h,x:x+w])
                labels.append(label)

train()
# print(f'Total train data is {len(images)} ={len(labels)}')
# print(labels)

face_recog=cv.face.LBPHFaceRecognizer_create()

# train
images=np.array(images,dtype='object')
labels=np.array(labels)
face_recog.train(images,labels)

face_recog.save('trained.yml')
np.save('images_of_faces_only.npy',images)
np.save('labels.npy',labels)








# 
# 