import kfb
import cv2
KFB = kfb.kfb('/home/xuehao/code_projs/WSI-SDK/data/test.kfb')
image = KFB.read()
image = image[::100, ::100, :]
print(image.shape)

cv2.imwrite('test.png',image)
# header = KFB.header()
