# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:51:38 2019

@author: Farhan
"""
import cv2
import numpy as np
img = cv2.imread("Before/*.jpg")
img = cv2.resize(img, (300,300), cv2.INTER_CUBIC)
cv2.imshow("img", img)


#UNTUK MEMBUAT GAMBAR MENJADI ABU-ABU (GRAYSCALING)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", img_gray)

#KITA MENCARI SENDIRI NILAI THRESHOLD NYA
#Fix Thresholding global
th, img_th1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

#OTSU MENCARI NILAI THRESHOLDING YANG PALING OPTIMAL
th, img_th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("img fix th", img_th1)
cv2.imshow("img otsu th", img_th2)

#edge detection
img_edge = cv2.Canny(img, 135,200)
cv2.imshow("edge detection", img_edge)

#segmentation (Mengambil yang mana foreground yang mana background)
ret, result = cv2.connectedComponents(img_th2)
idx = 0
background = np.zeros(img_th2.shape, np.uint8)
for res in np.unique(result):
    if res == 0:
        continue
    temp_obj = np.zeros(img_th2.shape, np.uint8)
    temp_obj[result ==res] = 255
   
    background = cv2.add(background, temp_obj)
    
conturs, hierarchy = cv2.findContours(background, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for idx_contur in conturs:
    x, y, w, h, = cv2.boundingRect(idx_contur)
    start = (x, y)
    end = (x + w, y + h)
    imgg = cv2.rectangle(img_th2, start, end, (255,0,0), 2)
    
cv2.imshow("segmentation", img)