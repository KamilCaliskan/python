import cv2 as cv
import numpy as np

img=cv.imread('1234.jpg',0)
kernel=np.ones((5,5),np.uint8)
erosion=cv.erode(img,kernel,iterations=1)

#dilation
dilation=cv.dilate(img,kernel,iterations=1)
#if atleast one pixel under the kernel is 1

#opening

opening=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)  
#it is useful in removing noise



closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)


gradient=cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)


tophat=cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)

blackhat=cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)

