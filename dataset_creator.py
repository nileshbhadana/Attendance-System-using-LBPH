#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 03:44:34 2018

@author: nilesh
"""
#importing libraries
import cv2,os
import numpy as np

try:
    os.mkdir("dataset_images")
except:
    print()

def image_taker(dir_name,student_id):
    counter=0
    cam=cv2.VideoCapture(0)
    '''width=640
    height = 480
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
    cam=cv2.VideoCapture("rtsp://192.168.10.240:554/onvif1",cv2.CAP_FFMPEG)

    cam.set(3,width)
    cam.set(4,height)'''
    #startin the loop
    while cam.isOpened():
        
        #readin the frame
        frame=cam.read()[1]
        #converting frame to gray
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #reading and detecting faces in the frame
        faces=cascade.detectMultiScale(gray_image,1.5,5)
        
        for (x,y,w,h) in faces:
            #drawing around the face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            counter=counter+1
            print(counter)
            
            #saving the face images
            cv2.imwrite(dir_name+"/image,"+str(student_id)+","+str(counter)+".jpg",gray_image)
            
            #showing the frame
        cv2.imshow('capturing images',frame)
    
    #handler
        if cv2.waitKey(50) & 0xFF==ord('q'):
            break
        elif cv2.waitKey(50) & counter>=20:
            student_id=student_id+1
            break
        
        #releasing the camera
    cam.release()
        #destroying all windows
    cv2.destroyAllWindows()

#casecading xml file
cascade=cv2.CascadeClassifier("face.xml")

#setting up student Id
choice='y'

while(choice=='y'):
    try:
        labels=np.load('training_ids.npy')
        student_id=max(labels)+1
    except:
        student_id=0


    print(student_id)

    student_name=input("Enter student name: ")
    
    #defining directory name where images will be stored
    dir_name="/home/nilesh/Desktop/attandance_system_face/dataset_images/"+student_name
    
    #using try to avoid error when directory is already present
    try:
        os.mkdir(dir_name)
        image_taker(dir_name,student_id)
    except:
        print("Student name already exits.")
    
    os.system("python3 trainer.py")
    choice=input("Add another:")
    
