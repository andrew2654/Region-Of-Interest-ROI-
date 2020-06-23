# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:28:06 2019

@author: USER
"""


import cv2
import numpy as np

global img2
#img = cv2.imread('C:/Users/Andrew LIU/Desktop/pic/GG.tiff',0)
#img2 = img.copy()  # 保證每次都重新在原圖畫

def CropImg_noExtract(x,y,w,h,img):
    global src, ROI, mask2,img2
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = img.copy()
    mask = np.zeros(img.shape, np.uint8)
    pts = np.array(([x, y], [x+w, y], [x+w, y+h], [x, y+h]), np.int32)  # pts是多邊形的頂點列表（頂點集）
    pts = pts.reshape((-1, 1, 2))
    # 這裡 reshape 的第一个參數為-1, 這一维的長度是根據後面的维度的計算出来的。
    # OpenCV中需要先將多邊形的頂點座標變成頂點数x1x2维的矩陣，再来繪制

    # --------------畫多邊形---------------------
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    ##-------------填充多邊形---------------------
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
#    cv2.imshow('mask', mask2)
#    cv2.waitKey(0)
    cv2.imwrite('mask.tiff', mask2)
    ROI = cv2.bitwise_and(mask2, img)
    cv2.imwrite('ROI.tiff', ROI)

    mask = np.zeros(img.shape, np.uint8)
    pts = np.array([[x, y], [x+w, y], [x+w, y+h], [x, y+h]],np.int32)# 頂點集
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))

    ROI = cv2.bitwise_and(mask2, img)
    cv2.imshow('ROI', ROI)
    cv2.waitKey(0)
    # cv2.imwrite('ROI.bmp', ROI)
    return ROI

# ------------------------------------------------------------
#ROI = img.copy()
#cv2.namedWindow('src')
#cv2.imshow("src",img)
cv2.waitKey(0)
cv2.destroyAllWindows()