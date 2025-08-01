import kfb
import cv2
import time


file_pth = '/home/xuehao/code_projs/WSI-SDK/data/test.kfb'


KFB = kfb.kfb(file_pth)
max_workers = 16

image = KFB.read(max_workers=max_workers)
image = image[::100, ::100, :]
print(image.shape)

cv2.imwrite('test.png',image)
# header = KFB.header()
