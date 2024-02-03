import cv2
import matplotlib.pyplot as plt
import numpy as np

def histogram(img):

    hist=np.zeros(256,np.uint32)
    height,width=img.shape

    for i in range (0,height):
        for j in range(0,width):
            hist[img[i][j]]+=1
    return hist

    
def thresholding(img):
    thresold_point=np.mean(img)
    height,width=img.shape

    for i in range (0,height):
        for j in range(0,width):
            if(img[i][j]>thresold_point):
                img[i][j]=255

            else:
                img[i][j]=0
    return img



def main():
    img=cv2.imread('images/skull.jpg',0)
    img=cv2.resize(img,(512,512))
    
    
    # plot original image
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('Orginal image')

    # plot original image histogram
    hist=histogram(img)
    plt.subplot(2,2,2)
    
    plt.bar(range(256),hist)
    plt.title('histogram of original image')


    # plot thresolding image
    img2=thresholding(img)
    plt.subplot(2,2,3)
    plt.imshow(img2,cmap='gray')
    plt.title('Thresolding image')


    # histogram of thresold image
    hist=histogram(img2)
    plt.subplot(2,2,4)
    plt.bar(range(256),hist)
    plt.title('histogram of Thresolding image')
    plt.show()

if __name__=="__main__":
    main()
