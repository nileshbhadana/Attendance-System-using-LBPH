#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 04:26:08 2018

@author: nilesh
"""
#importing libraries
import cv2,os
import numpy as np

#casecading the xml file
cascade=cv2.CascadeClassifier("face.xml")

face_datas=[]
ids=[]
id=0

#definig directory name where image data is stored
dir_name="/home/nilesh/Desktop/attandance_system_face/dataset_images/"
folder_name=os.listdir(dir_name)
for i in folder_name:
    print(i)
    student_dir_name=dir_name+str(i)
    face_names=os.listdir(student_dir_name)

#creating blank list to save face_data and label
    

    for image_name in face_names:
    
        #creating image path
        image_path=student_dir_name+"/"+image_name
        print(image_path)
    
        #reading image data in gray fromat
        face_data=cv2.imread(image_path,0)
        faces=cascade.detectMultiScale(face_data,1.5,5)
        print(faces)
        for (x,y,w,h) in faces:
        
            #appending data in lists
            face_datas.append(face_data[y:y+h,x:x+w])
            id=image_name.split(",")[-2]
            id=int(id)
            print(id)
            ids.append(id)
    

np.save('training_faces', face_datas)
np.save('training_ids', ids)
