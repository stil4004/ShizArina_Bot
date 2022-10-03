import numpy as np

im1 =  open('Arina(Helmet).jpg', 'rb')
im2 =  open('Arina(GN).jpg', 'rb')
print(calcdiff(im1, im2))


def calcdiff(im1, im2):
    dif = ImageChops.difference(im1, im2)
    return np.mean(np.array(dif))