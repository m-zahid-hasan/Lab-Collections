import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('images/Boundary_Extraction.png',0)
img=cv2.resize(img,(512,512))

def erosion(img,mask):
    row,col=img.shape
    temp=np.zeros((row,col),dtype=np.uint8)

    for r in range (0,row):
        for c in range (0,col):
            cnt=0
            for i in range (0,3): 
                for j in range (0,3):
                    nr=i+r-1
                    nc=j+c-1
                    if(nr>=0 and nc>=0) and (nr<row and nc<col):
                        if (mask[i][j]==1 and img[nr][nc]==1):
                            cnt+=1
            if (cnt==5):
                temp[r,c]=1
    return temp



struct_element=[[0,1,0],
                [1,1,1],
                [0,1,0]]
img=img/256
img=np.floor(img*2)
img=np.uint8(img)

img2=erosion(img,struct_element)
img2=img-img2
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.imshow(img2,cmap='gray')




plt.show()




# -----------------29/01/2024 exam day practise_________________
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# def erosion(img ,mask):
#     height,width=img.shape
#     temp=np.zeros((height,width),dtype=np.uint8)
#     pad=len(mask)//2
#     pad_img=np.pad(img,((pad,pad),(pad,pad)))
    
#     for r in range (height):
#         for c in range (width):
#             cnt=0
#             for i in range(0,len(mask)):
#                 for j in range (0,len(mask)):
#                     if (mask[i][j]==1 and pad_img[r+i][c+j]==1):
#                         cnt+=1
#             if cnt==5:
#                 temp[r,c]=1
#     return temp


# def dilation(img,mask):
#     height,width=img.shape
#     pad=len(mask)//2
#     temp=np.zeros((height,width),dtype=np.uint8)
#     pad_img=np.pad(img,((pad,pad),(pad,pad)))
    
#     for r in range (height):
#         for c in range (width):
#             cnt=0
#             for i in range (0,len(mask)):
#                 for j in range (0,len(mask)):
#                     if (mask[i][j]==1 and pad_img[r+i][c+j]==1):
#                         cnt+=1
#             if cnt !=0:
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


# def boundary_extraction(img,mask):
#     erosion_img=erosion(img,mask)
#     extraction=img-erosion_img
#     return extraction



# def main():
#     # img=cv2.imread('images/Boundary_Extraction.png',0)
#     img=cv2.imread('images/finger.jpg',0)
#     img = cv2.resize(img,(512,512))
#     orignial_img=img.copy()
    
#     img=img/256
#     img=np.floor(img*2)
#     img=np.uint8(img)
    
    
#     plt.subplot(3,3,1)
#     plt.imshow(img,cmap='gray')
#     plt.title('original image')
#     mask=[[0,1,0],
#           [1,1,1],
#           [0,1,0]]
#     erosion_img=erosion(img,mask)
#     plt.subplot(3,3,2)
#     plt.imshow(erosion_img,cmap='gray')
#     plt.title('erosion image')
    
#     dilation_img=dilation(img,mask)
#     plt.subplot(3,3,3)
#     plt.title('dilation img')
#     plt.imshow(dilation_img,cmap='gray')
    
    
#     opening_img=opening(img,mask)
#     plt.subplot(3,3,4)
#     plt.imshow(opening_img,cmap='gray')
#     plt.title('opeing image')
    
    

    
#     closing_img=closing(img,mask)
#     plt.subplot(3,3,5)
#     plt.imshow(closing_img,cmap='gray')
#     plt.title('closing img')
    
    
    
    
    
#     extraction=boundary_extraction(img,mask)
#     plt.subplot(3,3,6)
#     plt.imshow(extraction,cmap='gray')
#     plt.title('extraction image')
    
#     plt.tight_layout()
#     plt.show()
    

# if __name__=='__main__':
#     main()
    