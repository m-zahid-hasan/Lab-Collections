import cv2
import matplotlib.pyplot as plt
import numpy as np


def intensity_resolution(img,bits):
    height,width=img.shape
    img2=np.zeros((height,width),dtype=np.uint8)
    L=2**bits
    

    for i in range ( 0 ,height ):
        for j in range( 0 , width ):
            temp=img[i][j]/256.0
            temp=np.uint8(np.floor(temp*L))
            img2[i][j]=temp
    
    return img2



def display(img_list):
    for i in range(0,len(img_list)):
        h,w=img_list[i].shape
        plt.subplot(3,3,i+1)
        plt.title(f'{8-i}-Bit Image')
        plt.imshow(img_list[i],cmap='gray')
        
    plt.tight_layout()
    plt.show()



def main():
    img=cv2.imread('images/brain.jpg',0)
    img=cv2.resize(img,(512,512))
    

    img_list=[]
    img_list.append(img)
    
    for i in range(7,0,-1):
        img2=intensity_resolution(img_list[0],i)
        img_list.append(img2)
    
    display(img_list)


if __name__=='__main__':
    main()
    


