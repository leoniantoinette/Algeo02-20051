import numpy as np
from svd import svd
from PIL import Image

#Membuka file Image dan pecah menjadi martriks r,g,b
def openImage(imagePath):
    originalImage = Image.open(imagePath)
    image = np.array(originalImage)

    imageRed = image[:, :, 0]
    imageGreen = image[:, :, 1]
    imageBlue = image[:, :, 2]

    return [imageRed, imageGreen, imageBlue, originalImage]

#kompress setiap r,g,b
def compression(A,k):
    #U_color, S_color, V_color = np.linalg.svd(A)
    U_color, S_color, V_color = svd(A)
    imgCompressed = np.zeros((A.shape[0],A.shape[1]))
    #tes print pake yg linalg sama fungsi svd kita
    # print(U_color[:, 0:k])
    # print(np.diag(S_color)[0:k,0:k])
    US = np.matmul(U_color[:, 0:k],np.diag(S_color)[0:k,0:k])
    imgReconstructed = np.matmul(US,V_color[0:k,:])
    imgCompressed = imgReconstructed.astype('uint8')
    return imgCompressed


r,g,b, originalImage = openImage('src/16.png')

k = 5

r_compressed = compression(r,k)
g_compressed = compression(g,k)
b_compressed = compression(b,k)

img_r = Image.fromarray(r_compressed, mode=None)
img_g = Image.fromarray(g_compressed, mode=None)
img_b = Image.fromarray(b_compressed, mode=None)

compressedImage = Image.merge("RGB",(img_r,img_g,img_b))
originalImage.show()
compressedImage.show()