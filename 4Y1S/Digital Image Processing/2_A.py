# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the image
# img = cv2.imread('images/a.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (512, 512))

# # Display the original image and its histogram
# plt.subplot(2, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('Original Image')

# plt.subplot(2, 2, 2)
# plt.hist(img.ravel(), bins=256, range=(0, 256))
# plt.title('Original Image Hist')

# # Define the range for intensity enhancement
# left = 0
# right = 50
# enhancement = 350

# # Convert the image to a floating-point format
# img = img.astype(float)
# output_img = img.copy()

# # Apply the intensity enhancement
# rows, columns = img.shape
# for i in range(rows):
#     for j in range(columns):
#         if left <= img[i, j] <= right:
#             output_img[i, j] = img[i, j] + enhancement
#         # Ensure pixel values are within the valid range [0, 255]
#         if output_img[i, j] < 0:
#             output_img[i, j] = 0
#         elif output_img[i, j] > 255:
#             output_img[i, j] = 255

# # Convert to uint8 data type
# output_img = output_img.astype(np.uint8)

# # Display the enhanced image and its histogram
# plt.subplot(2, 2, 3)
# plt.imshow(output_img, cmap='gray')
# plt.title('Range intensity enhancement')

# plt.subplot(2, 2, 4)
# plt.hist(output_img.ravel(), bins=256, range=(0, 256))
# plt.title('Output Image Hist')

# plt.show()





#                code without build in function
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('images/a.jpg',0)
img=cv2.resize(img,(512,512))

def function(img):
    row,col=img.shape
    start_point=int(input('Enter the starting point '))
    end_point=int(input('Enter the ending point'))
    add=int(input('Enter how much waant to add '))

    img2=np.zeros((row,col),dtype=np.uint8)

    for i in range (0,row):
        for j in range (0,col):
            temp=0
            if (img[i][j]>start_point and img[i][j]>end_point):
                temp=img[i][j]+add
            if (temp==0):
                img2[i][j]=img[i][j]
            elif (temp>255):
                img2[i][j]=255
            else:
                img2[i][j]=temp
    return img2


plt.subplot(2,1,1,)
plt.imshow(img,cmap='gray')
plt.title('orginal image')

img3=function(img)
plt.subplot(2,1,2)
plt.imshow(img3,cmap='gray')
plt.title('enhancement image')
plt.show()




