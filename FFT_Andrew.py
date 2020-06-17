# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:16:46 2019

@author: Andrew LIU
ㄋasdas"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
img = cv2.imread('C:/Users/Andrew LIU/Desktop/pic/1-CeO2_100k.tif',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


# 產生頻譜遮罩
rows, cols = img.shape
crow,ccol = int(rows/2), int(cols/2)
mask = np.ones((rows,cols),np.uint8)
mask[crow-275:crow+275, ccol-5:ccol+5] = 0
mask[crow-20:crow+20, ccol-5:ccol+5] = 1

# 施加頻譜遮罩
fshift2 = fshift*mask

# 逆轉換回空間域
i = np.fft.ifftshift(fshift2)
img_back = np.fft.ifft2(i)
img_back = np.abs(img_back)

# 施加遮罩後的頻譜值
magnitude_spectrum = 20*np.log(np.abs(fshift2))

plt.subplot(121),plt.imshow(img_back, cmap = 'gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Masked Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()