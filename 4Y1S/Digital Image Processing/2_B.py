# import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# img=cv2.imread("images/a.jpg",0)
# img=cv2.resize(img,(512,512))
# height,widht=img.shape

# orginal_img=img.copy()
# img1=img/255.0
# c=255/np.log(1+np.max(img))

# power_img=np.zeros((height,widht))
# inverse_log=np.zeros((height,widht))


# for i in range (0,height):
#     for j in range (0,widht):
#         power_img[i][j]=img1[i][j]**2
#         inverse_log[i][j]=np.exp(img1[i][j])**(1/c)-1


# plt.subplot(2,2,1)
# plt.imshow(orginal_img,cmap='gray')

# plt.subplot(2,2,2)
# plt.imshow(power_img,cmap='gray')

# plt.subplot(2,2,3)
# plt.imshow(inverse_log,cmap='gray')
# plt.title("inverse log")

# plt.show()
# cv2.waitKey(0)


# 11-12-2023
import matplotlib.pyplot as plt
import numpy as np
import cv2
import math


img=cv2.imread('images/a.jpg',0)
img=cv2.resize(img,(512,512))


def powerlaw(img):
    row,col=img.shape
    img2=np.zeros((row,col),dtype=np.uint8)
    for i in range (0,row):
        for j in range (0,col):
            pixel=(img[i][j]/255.0)**0.5
            img2[i][j]=pixel*255
    return img2



def inverlog(img):
    row ,col=img.shape
    img2=np.zeros((row,col),dtype=np.uint8)
    img=img/255
    c=255/np.log(1+255)

    for i in range (0,row):
        for j in range(0,col):
            pixel=np.exp(img[i][j]/c)-1
            img2[i][j]=pixel*255
    return img2


plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('orginal image')

img2=powerlaw(img)
plt.subplot(2,2,2)
plt.imshow(img2,cmap='gray')
plt.title('power image')

img3=inverlog(img)
plt.subplot(2,2,3)
plt.imshow(img3,cmap='gray')
plt.title('inverse log')


img4=cv2.absdiff(img2,img3)
plt.subplot(2,2,4)
plt.imshow(img4,cmap='gray')
plt.title('difference image')

plt.show()