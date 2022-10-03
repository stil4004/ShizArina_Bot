import numpy as np

im1 =  open('Арина(шлем).jpg', 'rb')
im2 =  open('Арина(спит нхй).jpg', 'rb')
print(calcdiff(im1, im2))


def calcdiff(im1, im2):
    dif = ImageChops.difference(im1, im2)
    return np.mean(np.array(dif))