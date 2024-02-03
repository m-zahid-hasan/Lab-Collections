import cv2
import matplotlib.pyplot as plt
import numpy as np


def add_guasianNoise(img):
    mean=5
    sd=12

    gaussian_noise=np.random.normal(mean,sd,img.shape) 
    gaussian_noise=np.uint8(gaussian_noise)
    noisy_img=cv2.add(img,gaussian_noise)
    return noisy_img


def FFF(noisy_img):
    noisy_img_fft=np.fft.fftshift(np.fft.fft2(noisy_img))
    return noisy_img_fft


def butterworthFilter(image,order,cut_of_frequency):
    height,width=image.shape
    butterworth_filter=np.zeros((height,width),dtype=np.float32)

    for u in range(height):
        for v in range(width):
            D=np.sqrt((u-height/2)**2+(v-width/2)**2)
            butterworth_filter[u,v]=1/(1+(D/cut_of_frequency)**(2*order))

    filtered_image=image*butterworth_filter
    filtered_image=np.fft.ifft2(np.fft.ifftshift(filtered_image))
    return np.abs(filtered_image)



def  gaussianFilter(image,cut_of_frequency):
    height,width=image.shape
    guassian_filter=np.zeros((height,width),dtype=np.float32)

    for u in range (height):
        for v in range(width):
            D=np.sqrt((u-height/2)**2+(v-width/2)**2)
            guassian_filter[u,v]=np.exp(-(D**2)/(2* (cut_of_frequency)**2))

    filtered_image=image*guassian_filter
    filtered_image=np.fft.ifft2(np.fft.ifftshift(filtered_image))
    return np.abs(filtered_image)







def main():
    img = cv2.imread('images/alphabet.jpg',0)
    img = cv2.resize(img,(512,512))


    plt.subplot (3,3,1)
    plt.title ('orignial image')
    plt.imshow (img,cmap='gray')


    noisy_img = add_guasianNoise(img)
    plt.subplot (3,3,2)
    plt.title ('noisy image')
    plt.imshow (noisy_img,cmap='gray')



    noisy_img_fft = FFF(noisy_img)
    
    filtered_image = butterworthFilter(noisy_img_fft,10,60)
    plt.subplot (3,3,3)
    plt.title ('Butterworth_image')
    plt.imshow (filtered_image,cmap='gray')


    filtered_image = gaussianFilter(noisy_img_fft,60)
    plt.subplot (3,3,4)
    plt.title ("Gaussian_filter_image")
    plt.imshow (filtered_image,cmap='gray')
    

    plt.tight_layout ()
    plt.show ()



if __name__=="__main__":
    main()
    

