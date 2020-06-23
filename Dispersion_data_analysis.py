# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:15:02 2019

@author: Andrew LIU
"""

import cv2
import numpy as np
import math



#處理輸入影像
def Dispersion(img):
    blurred, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 自動輸入照片高跟寬
    h,w =img.shape
    rh = h/h
    rw = w/1

# 定義處存位置
    dispersion = []
# 計算長度
    def Length(Pt1, Pt2):
        L = math.sqrt((Pt1[0] - Pt2[0]) ** 2 + (Pt1[1] - Pt2[1]) ** 2)
        return L
    def SortTuple(tup):
        return(sorted(tup, key = lambda x : x[0]))
#移動至下一格進行ROI擷取
    M = 1
    for z in range(1,h):
        img_slice = blurred[z-int(rh)*M:z, 0:int(rw)]
        edges = cv2.Canny(img_slice, 100, 200)
        indices = np.where(edges != [0])
        coordinates = zip(indices[1],indices[0])
        sort_coord = SortTuple(coordinates)
        ListX = []
        ListY = []
        for i in range(0,len(sort_coord)):
            ListX.append(sort_coord[i][0])
            ListY.append(sort_coord[i][1])
            
        for i in range(0,len(ListX)-1):
            centerX = int((ListX[i] + ListX[i + 1]) / 2)
            centerY = int((ListY[i] + ListY[i + 1]) / 2)
            if img_slice[0,centerX] == 255:
                dispersion.append(Length([ListX[i],ListY[i]] , [ListX[i+1],ListY[i+1]]))

# Vertical Scan
    for z in range(1,w):
        img_slice = blurred[0:h, z-1*M:z]
        edges = cv2.Canny(img_slice, 100, 200)
        indices = np.where(edges != [0])
        coordinates = zip(indices[1], indices[0])
        sort_coord = SortTuple(coordinates)
        ListX = []
        ListY = []
        for i in range(0, len(sort_coord)):
            ListX.append(sort_coord[i][0])
            ListY.append(sort_coord[i][1])

        for i in range(0, len(ListX) - 1):
            centerX = int((ListX[i] + ListX[i + 1]) / 2)
            centerY = int((ListY[i] + ListY[i + 1]) / 2)
            if img_slice[centerY, 0] == 255:
                dispersion.append(Length([ListX[i], ListY[i]], [ListX[i + 1], ListY[i + 1]]))
    return dispersion