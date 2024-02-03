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
    return temp



def compute_psnr(img1,img2):
    img1,img2=np.float64(img1),np.float64(img2)
    mse=np.mean((img1-img2)**2)

    if mse==0.0:
        return float('inf')
    psnr=20*np.log10(255.0)-10*np.log10(mse)
    return np.round(psnr,2)



def main():
    img = cv2.imread ('images/alphabet.jpg',0)
    img = cv2.resize(img,(512,512))
    orginal_img = img.copy()


    plt.subplot (3,2,1)
    plt.imshow (img,cmap='gray')
    plt.title ('original image')


    noisy_img = addSaltandPepperNoise(img)
    plt.subplot (3,2,2)
    plt.imshow (noisy_img,cmap='gray')
    psnr1 = compute_psnr (orginal_img,noisy_img)
    plt.title (f'noisy image psnr : {psnr1}')

    # filter 3x3
    filtered_img1 = averageFilter ( noisy_img, 3 )
    plt.subplot (3,2,3)
    psnr1 = compute_psnr ( orginal_img, filtered_img1 )
    plt.imshow (filtered_img1, cmap = 'gray')
    plt.title ( f'mask size 3x3, psnr : {psnr1}')

    # mask size 5x5
    filtered_img2 = averageFilter (noisy_img, 5)
    plt.subplot(3,2,4)
    psnr2 = compute_psnr ( orginal_img, filtered_img2)
    plt.imshow (filtered_img2, cmap = 'gray')
    plt.title (f'mask size 5x5, psnr : {psnr2}')

    # mask size 7x7
    filtered_img3 = averageFilter (noisy_img, 7)
    plt.subplot (3,2,5)
    psnr3=compute_psnr (orginal_img, filtered_img3)
    plt.imshow (filtered_img3, cmap = 'gray')
    plt.title (f'mask size 7x7, psnr : {psnr3}')




    plt.tight_layout()
    plt.show()


if __name__=="__main__":
    main()
