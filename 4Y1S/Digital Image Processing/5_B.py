import numpy as np 
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('images/finger.jpg',0)
img=cv2.resize(img,(512,512))



def erosion(img,mask):
    row,col=img.shape
    temp=np.zeros((row,col),dtype=np.uint8)

    for r in range (0,row):
        for c in range(0,col):
            cnt=0
            for i in range (0,len(mask)):
                for j in range (0,len(mask)):
                    nr=i+r-1
                    nc=j+c-1
                    if (nr>=0 and nc>=0) and (nr<row and nc<col):
                        if (mask[i][j]==1 and img[nr][nc]==1):
                            cnt+=1
            if (cnt==9):
                temp[r][c]=1
    return temp


def dilation(img,mask):
    row,col=img.shape
    temp=np.zeros((row,col),dtype=np.uint8)

    for r in range (0,row):
        for c in range (0,col):
            cnt=0
            for i in range (0,len(mask)):
                for j in range(0,len(mask)):
                    nr=i+r-1
                    nc=j+c-1
                    if (nr>=0 and nc>=0) and (nr<row and nc<col):
                        if (mask[i][j]==1 and img[nr][nc]==1):
                            cnt+=1
            if (cnt>0):
                temp[r][c]=1
    return temp


def opening(img,mask):
    temp=erosion(img,mask)
    temp=dilation(temp,mask)
    return temp

def closing(img,mask):
    temp=dilation(img,mask)
    temp=erosion(temp,mask)
    return temp






SE=[[1,1,1],
      [1,1,1],
      [1,1,1]]
img=img/256
img=np.floor(img*2)
img=np.uint8(img)


img2=opening(img,SE)

plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.imshow(img2,cmap='gray')

img3=closing(img,SE)
plt.subplot(2,2,3)
plt.imshow(img3,cmap='gray')


plt.show()



# --------------29/01/2024
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np


# def erosion(img,mask):
#     height,width=img.shape
#     temp=np.zeros((height,width),dtype=np.uint8)
#     pad=len(mask)//2
#     pad_img=np.pad(img,((pad,pad),(pad,pad)))
    
#     for r in range(height):
#         for c in range(width):
#             cnt=0
#             for i in range(0,len(mask)):
#                 for j in range(0,len(mask)):
#                     if (mask[i][j]==1 and pad_img[r+i][c+j]==1):
#                         cnt+=1
#             if cnt==5:
#                 temp[r,c]=1
#     return temp


# def dilation(img,mask):
#     height,width=img.shape
#     temp=np.zeros((height,width),dtype=np.uint8)
#     pad=len(mask)//2
    
#     pad_img=np.pad(img,((pad,pad),(pad,pad)))
    
#     for r in range (height):
#         for c in range (width):
#             cnt=0
#             for i in range (len(mask)):
#                 for j in range(len(mask)):
#                     if (mask[i][j]==1 and pad_img[r+i][c+j]==1):
#                         cnt+=1
#             if cnt!=0:
#                 temp[r,c]=1
#     return temp



# def opening(img,mask):
#     erosion_img=erosion(img,mask)
#     dilation_img=dilation(erosion_img,mask)
#     return dilation_img

# def closing(img,mask):
#     dilation_img=dilation(img,mask)
#     erosion_img=erosion(dilation_img,mask)
#     return erosion_img
    

# def main():
#     img =cv2.imread('images/finger.jpg',0)
#     img=cv2.resize(img,(512,512))
#     orginal_img=img.copy()
    
    
#     img=img/256.0
#     img=np.floor(img*2)
#     img=np.uint8(img)
    
    
#     plt.subplot(2,2,1)
#     plt.title('original image')
#     plt.imshow(orginal_img,cmap = 'gray')
    
#     mask=[[0,1,0],
#           [1,1,1],
#           [0,1,0]]
    
#     # erosion_img=erosion(img,mask)
#     # plt.subplot(2,2,2)
#     # plt.imshow(erosion_img,cmap='gray')
#     # plt.title('erosion image')
    
    
#     # dilation_img=dilation(erosion_img,mask)
#     # plt.subplot(2,2,3)
#     # plt.imshow(dilation_img,cmap='gray')
#     # plt.title('dilation image')
#     # opening_img=opening(img,mask)
#     # plt.subplot(2,2,2)
#     # plt.imshow(opening_img,cmap='gray')
#     # plt.title('closing image')
    
    
#     closing_img=closing(img,mask)
#     plt.subplot(2,2,3)
#     plt.imshow(closing_img,cmap='gray')
#     plt.title('closing image')
    
    
#     plt.show()


# if __name__=='__main__':
#     main()
    
    
    
    
    
    