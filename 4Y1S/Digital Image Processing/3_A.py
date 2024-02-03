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
    
    for i in range(number_of_pixels):
        x=np.random.randint(0,height-1)
        y=np.random.randint(0,width-1)
        temp[x,y]=0
    return temp


def averageFilter(img,mask):
    height,width=img.shape
    temp=img.copy()
    pad=mask//2
    pad_img=np.pad(img,((pad,pad),(pad,pad)))


    for r in range(0,height):
        for c in range(0,width):
            sum=0
            for i in range (0,mask):
                for j in range(0,mask):
                    sum+=pad_img[r+i][c+j]
            temp[r,c]=(sum/(mask*mask))
    return np.uint8(temp)


def medianFilter(img,mask):
    height,width=img.shape
    temp=img.copy()
    pad=mask//2
    pad_img=np.pad(img,((pad,pad),(pad,pad)))

    for r in range (0,height):
        for c in range(0,width):
            neigherbor=[]
            for i in range(0,mask):
                for j in range(0,mask):
                    x=pad_img[r+i][c+j]
                    neigherbor.append(x)
            neigherbor=sorted(neigherbor)
            temp[r,c]=neigherbor[len(neigherbor)//2]
    return temp
            

def compute_psnr(img1,img2):
    img1,img2=np.float64(img1),np.float64(img2)
    mse=np.mean((img1-img2)**2)

    if mse==0.0:
        return float('inf')
    psnr=20*np.log10(255.0)-10*np.log10(mse)
    return np.round(psnr,2)


def main():
    img=cv2.imread('images/alphabet.jpg',0)
    img=cv2.resize(img,(512,512))
    orginal_img=img.copy()


    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original image')

    noisy_img=addSaltandPepperNoise(img)
    plt.subplot(2,2,2)
    plt.imshow(noisy_img,cmap='gray')
    psnr1=compute_psnr(orginal_img,noisy_img)
    plt.title(f'noisy image psnr : {psnr1}')
    
    
    filtered_img = averageFilter (noisy_img, 5)
    plt.subplot (2, 2, 3)
    plt.imshow (filtered_img, cmap='gray' )
    psnr2=compute_psnr (orginal_img, filtered_img)
    plt.title (f'average filter psnr: {psnr2}')

    # compare average filter using built in function cv2.blur(img,(mask,mask))
    # plt.subplot(2,2,4)
    # plt.imshow(cv2.blur(noisy_img,(5,5)),cmap='gray')
    # plt.title('averageFilter')

    filtered_img=medianFilter(noisy_img,5)
    plt.subplot(2,2,4)
    psnr3=compute_psnr (orginal_img, filtered_img)
    plt.imshow(filtered_img,cmap='gray')
    plt.title(f'median filter psnr :{psnr3}')

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()


