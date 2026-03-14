import cv2
import numpy as np
import os

image1 = cv2.imread("tree.jpg")
#the order is top,bottom,left,right
bordered_image = cv2.copyMakeBorder(image1,20,20,20,20,cv2.BORDER_CONSTANT,value=1)

cv2.imshow("original image",image1)
cv2.imshow("bordered image",bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()













