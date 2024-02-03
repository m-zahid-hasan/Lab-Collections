import cv2
import matplotlib.pyplot as plt
import numpy as np


def spatial_resolution(img):
    img_list=[]
    img_list.append(img)
    f=2

    for i in range(0,8):
        height,width=img.shape
        img2=np.zeros((height//2,width//2),dtype=np.uint8)

        for j in range(0,height//2):
            for k in range(0,width//2):
                img2[j][k]=img[j*f][k*f]

        img_list.append(img2)
        img=img2
    
    return img_list



def display(img_list):
    for i in range(0,len(img_list)):
        plt.subplot(3,3,i+1)
        plt.imshow(img_list[i],cmap='gray')
        h,w=img_list[i].shape
        plt.title(f'{h}x{w}')
    plt.tight_layout()
    plt.show()


def main():
    
    img=cv2.imread('images/a.jpg',0)
    img=cv2.resize(img,(512,512))
    img_list=[]

    img_list=spatial_resolution(img)
    display(img_list)

if __name__=='__main__':
    main()

