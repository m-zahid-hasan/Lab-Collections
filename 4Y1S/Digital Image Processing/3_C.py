# import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# img=cv2.imread("images/a.jpg",0)
# img=cv2.resize(img,(512,512))

# row,col=img.shape
# img2=img.copy()
# # print(img)
# for i in range (1,row-1):
#     for j in range (1,col-1):
#         temp=img[i-1,j-1]*img[i-1,j]*img[i-1,j+1]*img[i,j-1]*img[i,j]*img[i,j+1]*img[i+1,j-1]*img[i+1,j]*img[i+1,j+1]
#         temp=(np.power(temp,(1/9)))
#         img2[i][j]=temp
#         # print(temp)

        
# print(img2)
# plt.subplot(2,1,1)
# plt.imshow(img,cmap='gray')
# plt.title('Orginal img')

# plt.subplot(2,1,2)
# plt.imshow(img2 ,cmap='gray')
# plt.title('Modified image')

# plt.show()
# cv2.waitKey(0)


import cv2
import matplotlib.pyplot as plt
import numpy as np
from math import log10,sqrt

img=cv2.imread("images/noisysalterpepper.png",0)
img=cv2.resize(img,(512,512))





def harmonicFilter(img,n):
    row,col=img.shape
    img2=np.copy(img)
    s=n//2

    for i in range (s,row-s):
        for j in range (s,col-s):
            sum=0
            for k in range(i-s,i+s+1):
                for l in range (j-s,j+s+1):
                    if (img[k,l]!=0):
                         sum+=1/img[k,l]
            if (sum!=0):
                img2[i,j]=(n*n)/sum 
    return img2




def geometricMeanFilter(img,n):
    row,col=img.shape
    img3=img.copy()

    s=n//2
    for i in range (s,row-s):
        for j in range (s,col-s):
            sum=1
            for k in range (i-s,i+s+1):
                for l in range (j-s,j+s+1):
                    if (img[k,l]!=0):
                         sum=sum*int(img[k,l])          
            img3[i,j]=((sum)**(1/(n*n)))
    return img3

    



plt.subplot(3,2,1)
plt.imshow(img,cmap='gray')
plt.title('orginal image')

n=int(input("take mask size :"))

img4=harmonicFilter(img,n)
plt.subplot(3,2,2)
plt.imshow(img4,cmap='gray')
plt.title("hermonic mean filter")


img5=geometricMeanFilter(img,n)
plt.subplot(3,2,3)
plt.imshow(img5,cmap='gray')

plt.show()




# 11-12-2023
# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import math
# from math import log10,sqrt
# import cv2

# img=cv2.imread('images/noisysalterpepper.png',0)
# img=cv2.resize(img,(512,512))

# def geometric(img,n):
#     row,col=img.shape
#     temp=np.zeros((row,col),dtype=np.uint8)
#     for r in range (0,row):
#         for c in range(0,col):
#             product=1
#             for i in range (0,n):
#                 for j in range (0,n):
#                     nr=i+r-1
#                     nc=j+c-1
#                     if(nr>=0 and nc>=0)and (nr<row and nc<col):
#                         if(img[nr][nc]!=0):
#                             product=product*int(img[nr][nc])
#             if (product>1):
#                 temp[r,c]=((product)**(1/(n*n)))
#     return temp


# def harmonic(img,n):
#     row,col=img.shape
#     temp=np.zeros((row,col),dtype=np.uint8)

#     for r in range(0,row):
#         for c in range(0,col):
#             sum=0
#             for i in range(0,n):
#                 for j in range(0,n):
#                     nr=i+r-1
#                     nc=j+c-1
#                     if(nr>=0 and nc>=0)and (nr<row and nc<col):
#                         sum=sum+1/img[nr][nc]
#             temp[r,c]=(n*n)/sum
#     return temp


# plt.subplot(2,2,1)
# plt.imshow(img,cmap='gray')
# plt.title('orginal image')

# plt.subplot(2,2,2)
# plt.imshow(geometric(img,3),cmap='gray')
# plt.title('geometric mean filter')

# plt.subplot(2,2,3)
# plt.imshow(harmonic(img,3),cmap='gray')
# plt.title('harmonic mean filter')

# plt.show()



#--------------------- 1/24/2024
import cv2
import matplotlib.pyplot as plt
import numpy as np



def addSaltandPepperNoise(img):
    number_of_pixels=np.random.randint(50000,90000)
    height,width=img.shape
    temp=img.copy()

    for i in range(number_of_pixels):
        x=np.random.randint(0,height-1)
        y=np.random.randint(0,width-1)
        temp[x,y]=255
    
    number_of_pixels2=np.random.randint(500,1000)
    
    # for i in range(number_of_pixels2):
    #     x=np.random.randint(0,height-1)
    #     y=np.random.randint(0,width-1)
    #     temp[x,y]=0
    return temp


def compute_psnr(img1,img2):
    img1,img2=np.float64(img1),np.float64(img2)
    mse=np.mean((img1-img2)**2)

    if mse==0.0:
        return float('inf')
    psnr=20*np.log10(255.0)-10*np.log10(mse)
    return np.round(psnr,2)


def geomtric_Mean_Filter(img,mask):
    ans = img.copy()
    height,width = img.shape
    pad=mask//2
    pad_img = np.pad(img,((pad,pad),(pad,pad)),mode='constant',constant_values=1)

    for r in range (0,height):
        for c in range (0,width):
            sum=1
            for i in range (0,mask):
                for j in range (0,mask):
                    if pad_img[r+i,c+j]!=0:
                        sum=sum*int(pad_img[r+i,c+j])
                    
            sum=sum**(1/(mask*mask))
            ans[r,c]=sum
    return ans
                    


def harmonic_filter(img,mask):
    ans = img.copy()
    height,width = img.shape
    pad = mask//2
    pad_img = np.pad(img,((pad,pad),(pad,pad)))
    
    for r in range (0,height):
        for c in range (0,width):
            sum = 0
            for i in range (0,mask):
                for j in range (0,mask):
                    sum+=1/(pad_img[r+i][c+j]+1e-6)
            if sum!= 0:
                sum = (mask*mask)/sum
                ans[r,c] = sum
                             
    return ans


def main():

    img = cv2.imread('images/motherboad.jpg',0)
    img = cv2.resize(img,(512,512))
    orginal_img=img.copy()


    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original image')

    noisy_img=addSaltandPepperNoise(img)
    plt.subplot(2,2,2)
    plt.imshow(noisy_img,cmap='gray')
    psnr1=compute_psnr(orginal_img,noisy_img)
    plt.title(f'noisy image psnr : {psnr1}')
    
    filtered_img = geomtric_Mean_Filter (noisy_img,5)
    plt.subplot (2,2,3)
    psnr2 =compute_psnr(img,filtered_img)
    plt.imshow (filtered_img,cmap = 'gray')
    plt.title(f'geometric mean filter psnr : {psnr2}')
    
    filtered_img=harmonic_filter (noisy_img,5)
    plt.subplot(2,2,4)
    psnr3=compute_psnr(orginal_img,filtered_img)
    plt.imshow(filtered_img,cmap='gray')
    plt.title(f'harmonic mean filter psnr : {psnr3}')
    
    
    plt.show()


if __name__=="__main__":
    main()
