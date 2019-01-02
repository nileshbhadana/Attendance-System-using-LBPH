#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:32:31 2019

@author: nilesh
"""

import cv2,os
width=1280
height = 720
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
cam_cap=cv2.VideoCapture("rtsp://192.168.10.112:554/onvif1",cv2.CAP_FFMPEG)

cam_cap.set(3,width)
cam_cap.set(4,height)

while cam_cap.isOpened():
	status,frame=cam_cap.read()
	cv2.imshow('live',frame)
	if cv2.waitKey(2) & 0xFF == ord('q'):		
		break
cv2.destroyAllWindows()
cam_cap.release()
