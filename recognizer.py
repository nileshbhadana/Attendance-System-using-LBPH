#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 05:19:44 2018

@author: nilesh
"""
#importing libraries
import cv2,time,os,datetime
import numpy as np

def save_att(student_id):
    #present=0
    print("hhhhh")
    d=datetime.date.today()
    ids=[]
    file_name=d.strftime("%d_%B"+".txt")
    try:
        with open(file_name,'r+') as file_data:
            for line in file_data:
                id,state=line.split(",")
                ids.append(int(id))
            if student_id not in ids:
                #present=1
                print("not present")
                file_data.write("\n"+str(student_id)+",p")
                file_data.seek(0)
                print("marked")
                    
    except FileNotFoundError:
        with open(file_name,'w') as file_data:
            file_data.write(str(student_id)+",p")
            print("file created")
#setting font for puttext
font=cv2.FONT_HERSHEY_SIMPLEX

val_list = ['hash',
    'account_url',
    'account_id',
    'title',
    'timestamp',
    'ext',
    'section',
    'animated',
    'hot_datetime',
    'meme_name',
    'num_images',
    'reddit',
    'topic',
    'virality',
    'ups',
    'downs',
    'views',
    'favorited',
    'comment_count',
    'score',
    'points',
    'nsfw',
    'is_album',
    'count_album_img',
    'album_still_share',
    'album_gif_share',
    'album_avg_img_size',
    'album_titles']

#Connect to database
connection = sqlite3.connect(outputdb)
c = connection.cursor()

#c.execute("DROP TABLE imagedata_" + input_ext + ";")

#If table exists, create a dictionary to store pre-scraped URLs. Otherwise, create the table.
scraped_values_dict = {}
try:
    for scraped_url in c.execute("SELECT hash FROM imagedata_"+ input_ext):
        scraped_values_dict[scraped_url] = ''
except sqlite3.OperationalError:
    c.execute("CREATE TABLE imagedata_" + input_ext + "(hash CHAR(20), account_url TEXT, account_id INT, title TEXT, timestamp TIMESTAMP, ext CHAR(6), section TEXT, animated INT, hot_datetime TIMESTAMP, meme_name TEXT, reddit TEXT, topic TEXT, virality FLOAT, ups INT, downs INT, views INT, favorited INT, comment_count INT, score INT, points INT, nsfw INT, is_album INT, album_images INT, album_still_share FLOAT, album_gif_share FLOAT, album_avg_img_size FLOAT, album_titles FLOAT )")
    connection.commit()
connection.close()
#loading and reading data from the saved training files
face_data=np.load('training_faces.npy')
labels=np.load('training_ids.npy')
print(labels)

#creating recognizer
recognizer=cv2.face.LBPHFaceRecognizer_create()

#training the recognizer
recognizer.train(face_data,np.array(labels))

#flag for the detected face
detected=0
#cascading
cascade=cv2.CascadeClassifier('face.xml')
# opening camera
'''width=640
height = 480
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
cam=cv2.VideoCapture("rtsp://192.168.10.240:554/onvif1",cv2.CAP_FFMPEG)

cam.set(3,width)
cam.set(4,height)
'''
cam=cv2.VideoCapture(0)

while cam.isOpened():
    # reading frame
    frame=cam.read()[1]
    #converting frame to gray 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    
    for (x,y,w,h) in faces:
        #drawing rectangle on the faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
        #predicting the label and confidence
        label,confidence=recognizer.predict(gray_frame[y:y+h,x:x+w])
        print(label)
        
        #checking for confidence (the lower the confidence the more accurate the prediction is)
        if confidence<70:
            save_att(label)
            if label==1:
                msg="salman"
            elif label==0:
                msg="nilesh"
            
            #printing the message 
            #cv2.putText(frame,msg,(x,y),font,1,(255,255,255),3,cv2.LINE_AA)
            
            #changing flag to 1
            detected=1
    cv2.imshow('live',frame)

    #handler
    if cv2.waitKey(2) & 0xFF == ord('q'):		
        break
    #elif cv2.waitKey(2) & detected==1:
     #   time.sleep(0.5)
      #  break
cv2.destroyAllWindows()
cam.release()


            
        
    
    
    
    
    
    
