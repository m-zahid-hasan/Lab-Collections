

#  5(a) erosion and dilation

import cv2
import matplotlib.pyplot as plt
import numpy as np


def padding_image(img,pading,pad):
    height,width=img.shape #(512,512)
    img2=np.zeros((height+pading,width+pading),dtype=np.uint8) #(514,514) padding=2
    
    #copy orginal image (img) intensity to padding image(img2) 
    for i in range(0,height):
        for j in range(0,width):
            img2[i+pad][j+pad]=img[i][j]
    return img2



def dilation(img2,sr,height,width,pad):
    r,c=img2.shape
    temp=np.zeros((height,width),dtype=np.uint8)

    for i in range (0,r-pad*2):
        for j in range(0,c-pad*2):
            cnt=0
            for k in range(0,3):
                for l in range(0,3):
                    if(sr[k][l]==1 and img2[i+k][j+l]==1):
                        cnt+=1
            if cnt!=0:
                temp[i][j]=1
    return temp



def erosion(img2,sr,height,width,pad):
    r,c=img2.shape
    temp=np.zeros((height,width),dtype=np.uint8)


    for i in range(0,r-pad*2):
        for j in range(0,c-pad*2):
            cnt=0
            for k in range(0,3):
                for l in range(0,3):
                    if (sr[k][l]==1 and img2[i+k][j+l]==1):
                        cnt+=1
            if cnt==5:
                temp[i][j]=1
    return temp


def main():
    img=cv2.imread('images/finger.jpg',0)
    img=cv2.resize(img,(512,512))

    img=img/256
    img=np.floor(img*2)
    img=np.uint8(img)

    sr=[[0,1,0],
        [1,1,1],
        [0,1,0]]
    
    height,width=img.shape
    padding=2*(len(sr)//2)
 
    pad=padding//2
    
    
    img2=padding_image(img,padding,pad)
    erosion_ans=erosion(img2,sr,height,width,pad)
    plt.subplot(2,2,1)
    plt.imshow(erosion_ans,cmap='gray')

    img3=padding_image(erosion_ans,padding,pad)
    dilation_ans=dilation(img3,sr,height,width,pad)
    plt.subplot(2,2,3)
    plt.imshow(dilation_ans,cmap='gray')

    plt.show()


if __name__=="__main__":
    main()

    


    

    