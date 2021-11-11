import numpy as np
import time
from svd import svd
from PIL import Image

#Membuka file Image dan pecah menjadi martriks r,g,b
def openImage(imagePath):
    originalImage = Image.open(imagePath)
    image = np.array(originalImage).astype(float)

    imageRed = image[:, :, 0]
    imageGreen = image[:, :, 1]
    imageBlue = image[:, :, 2]

    return [imageRed, imageGreen, imageBlue, originalImage]

#kompress setiap r,g,b
def compression(A,k):
    U_color, S_color, V_color = svd(A)
    imgCompressed = np.zeros((A.shape[0],A.shape[1]))
    imgReconstructed = U_color[:, 0:k] @ (S_color)[0:k,0:k] @ V_color[0:k,:]
    imgCompressed = np.clip(imgReconstructed,0,255).astype('uint8')
    return imgCompressed

np.set_printoptions(suppress=True)

r,g,b, originalImage = openImage('src/72.png')

#input user
k = 50

#start_time = time.time()
r_compressed = compression(r,k)
g_compressed = compression(g,k)
b_compressed = compression(b,k)

img_r = Image.fromarray(r_compressed, mode=None)
img_g = Image.fromarray(g_compressed, mode=None)
img_b = Image.fromarray(b_compressed, mode=None)

#combine rgb
compressedImage = Image.merge("RGB",(img_r,img_g,img_b))
originalImage.show()
compressedImage.show()
final_time = time.time()

#print(final_time - start_time)

#Melihat perbandingan sebelum dan sesudah dikompres
# image = np.array(Image.open('src/72.png'))

# row = image.shape[0]
# col = image.shape[1]
# print('pixels: ', row ,'x',col)
# originalSize = row * col * 3
# compressedSize = k * (1 + row + col) * 3

# print('original size:')
# print(originalSize)

# print('compressed size:')
# print(compressedSize)

# print('Ratio compressed size / original size:')
# ratio = compressedSize/originalSize
# print(ratio)

# print('Compressed image size is ' + str(round(ratio * 100, 2)) + '% of the original image ')