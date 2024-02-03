import cv2
import matplotlib.pyplot as plt
import numpy as np


def add_guasianNoise(img,mean,sd):
    gaussian_noise=np.random.normal(mean,sd,img.shape)
    gaussian_noise=np.uint8(gaussian_noise)
    noisy_img=cv2.add(img,gaussian_noise)
    return noisy_img


def FFT(noisy_img):
    noisy_img_fft=np.fft.fftshift(np.fft.fft2(noisy_img))
    return noisy_img_fft


def idealLowpassFilter(image,cut_of_frequency):
    height,width=image.shape

    ideal_low_passFilter=np.zeros((height,width),dtype=np.uint8)

    for u in range(height):
        for v in range(width):
            D=np.sqrt((u-height/2)**2+(v-width/2)**2)
            if D<=cut_of_frequency:
                ideal_low_passFilter[u,v]=1
    
    filtered_image=image*ideal_low_passFilter
    filtered_image=np.fft.ifft2(np.fft.ifftshift(filtered_image))
    return np.abs(filtered_image)



def main():
    img=cv2.imread('images/alphabet.jpg',0)
    img=cv2.resize(img,(512,512))



    plt.subplot(3,2,1)
    plt.title('orginal image')
    plt.imshow(img,cmap='gray')


    noisy_img=add_guasianNoise(img,7,13)
    # plt.subplot(2,2,2)
    # plt.imshow(noisy_img,cmap='gray')
    # plt.title('Noisy image')


    noisy_img_fft=FFT(noisy_img)
    cut_of_frequency=0

    for i in range(1,6):
        cut_of_frequency+=10


        filtered_image=idealLowpassFilter(noisy_img_fft,cut_of_frequency)
        plt.subplot(3,2,i+1)
        plt.imshow(filtered_image,cmap='gray')
        plt.title(f"idealLowPassFilter D:{cut_of_frequency}")


    plt.tight_layout()
    plt.show()



if __name__=="__main__":
    main()


    
