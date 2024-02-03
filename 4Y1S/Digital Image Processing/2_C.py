import matplotlib.pyplot as plt
import cv2
import numpy as np

img=cv2.imread('images/a.jpg',0)
img=cv2.resize(img,(512,512))

mask=0b11100000

img2=img.copy()

height,widht=img.shape
for i in range (0,height):
    for j in range (0,widht):
        img2[i,j]=img2[i,j]&mask


plt.subplot(2,1,1)
plt.imshow(img,cmap='gray')

plt.subplot(2,1,2)
plt.imshow(img2,cmap='gray')
plt.show()
