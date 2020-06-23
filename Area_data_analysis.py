# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:57:01 2019

@author: Andrew LIU
"""

import cv2
import numpy as np



#frame = cv2.imread('C:/Users/Andrew LIU/Desktop/pic/GG_2.tiff' )
#frame = cv2.imread("C:/Users/Andrew LIU/Desktop/CIRCLE_BW.png")
frame = cv2.imread("C:/Users/Andrew LIU/Desktop/0919_binary_binary.tiff")
if frame is None:
    print("ERROR LOADING IMAGE")
    exit()

#img_chs = cv2.split(frame)

#binimg = (img_chs[2]>100)
#binimg = binimg.astype(np.uint8)
#distmap = cv2.distanceTransform(binimg,1,3)

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
#    binaryIMG = cv2.Canny(blurred, 20, 160)
ret, blurred = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
blurred, contours, hierarchy = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
areas = []
for i in range(0, len(contours)):
    areas.append(cv2.contourArea(contours[i]))


#binimg = (img_chs[2]>100)
#binimg = binimg.astype(np.uint8)
#distmap = cv2.distanceTransform(binimg,1,3)

#out = distmap*0
#ksize=10
#for x in range(ksize,distmap.shape[0]-ksize*2):
 #   for y in range(ksize,distmap.shape[1]-ksize*2):
  #      if distmap[x,y]>0 and distmap[x,y]==np.max(distmap[x-ksize:x+ksize,y-ksize:y+ksize]):
   #         out[x,y]=1

#out = cv2.dilate(out,(3,3))

#_ , contours, hier = cv2.findContours(out.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

arr=[]
Area=[]
for i in contours:
    x_=0
    y_=0
    for j in i:
        x_ += j[0][0]
        y_ += j[0][1]
    arr.append([x_/len(i), y_/len(i)])
arr = np.array(arr)

#    for i in range(0, len(contours)):#---------------------------------------------------
#        print('arr', (i + 1), ':', arr[i])
for i in range(0, len(contours)):#--------------------------------------------------
    Area.append(areas[i])
    print("areas",(i + 1),":",areas[i])
Area = np.array(Area,dtype=np.uint8)