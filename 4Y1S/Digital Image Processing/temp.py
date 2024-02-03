import cv2
import matplotlib.pyplot as plt
import numpy as np

def add_gausian_noise(img,mean,sd):
    gausian_noise=np.random.normal(mean,sd,img.shape)
    gausian_noise=np.uint8(gausian_noise)
    noisy_img=cv2.add(img,gausian_noise)
    return noisy_img

def FFT(noisy_img):
    noisy_img_fft=np.fft.fftshift(np.fft.fft2(noisy_img))
    return noisy_img_fft


def butterworth_filter (image,order,cut_of_f):
    height,width=image.shape
    filterr=np.zeros((height,width),dtype=np.float32)
    
    for u in range (height):
        for v in range (width):
            D=np.sqrt((u-height/2)**2+(v-height/2)**2)
            filterr[u,v]=1/(1+(D/cut_of_f)**(2*order))
    
    filter_img=image*filterr
    filter_img=np.fft.ifft2(np.fft.ifftshift(filter_img))
    # filter_img=np.abs(filter_img)
    return np.abs(filter_img)


def gaussian ( image,cut_of_f ):
    height,width=image.shape
    filterr=np.zeros((height,width),dtype=np.float32)
    
    for u in range (height):
        for v in range (width):
            D=np.sqrt((u-height/2)**2+(v-width/2)**2)
            filterr[u,v]=np.exp(-(D**2/(2*cut_of_f)**2))
    
    filter_img=filterr*image
    filter_img=np.fft.ifft2(np.fft.ifftshift(filter_img))
    # filter_img=np.abs(filter_img)
    return np.abs(filter_img)


def ideal (image,cut_of_f):
    height,width=image.shape
    filterr=np.zeros((height,width),dtype=np.float32)
    
    for u in range (height):
        for v in range (width):
            D=np.sqrt ((u-height/2)**2+(u-width/2)**2)
            if D<=cut_of_f:
                filterr[u,v]=1
   
    filter_img=image*filterr
    filter_img=np.fft.ifft2(np.fft.ifftshift(filter_img))
    return np.abs(filter_img)


def ideal_H(image,cut_of_f):
    height,width=image.shape
    filterr=np.zeros((height,width),dtype=np.float32)
    
    for u in range (height):
        for v in range (width):
            D=np.sqrt ((u-height/2)**2+(u-width/2)**2)
            if D>=cut_of_f:
                filterr[u,v]=1
    
    filter_img=image*filterr
    filter_img=np.fft.ifft2(np.fft.ifftshift(filter_img))
    return np.abs(filter_img)


def main():
    img=cv2.imread('images/alphabet.jpg',0)
    img=cv2.resize(img,(512,512))
    
    
    
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original image')
    
    noisy_img = add_gausian_noise(img,7,13)
    
    plt.subplot (2,2,2)
    plt.imshow (noisy_img,cmap='gray')
    plt.title('noisy image')
    
    noisy_img_fft=FFT(noisy_img)
    
    filtered_img=butterworth_filter(noisy_img_fft,6,30)
    plt.subplot(2,2,3)
    plt.imshow(filtered_img,cmap='gray')
    plt.title('butterworth filter')
    
    
    # filtered_img=gaussian (noisy_img_fft,30)
    # plt.subplot(2,2,4)
    # plt.imshow(filtered_img,cmap='gray')
    # plt.title('gaussian filter')
    
    
    
    # filter_img=ideal(noisy_img_fft,30)
    # plt.subplot(2,2,4)
    # plt.imshow(filter_img,cmap='gray')
    # plt.title('ideal filter')
    
    
    high_pass_fft=FFT(img)
    filter_img=ideal_H(high_pass_fft,50)
    plt.subplot(2,2,4)
    plt.imshow(filter_img,cmap='gray')
    plt.title('high pass filter')
    
    
    plt.show()
    
    

if __name__=='__main__':
    main()
    