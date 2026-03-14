import cv2
import numpy as np
import os

image1 = cv2.imread("lhama2.jpg")
median_blur = cv2.medianBlur(image1,5)
cv2.imshow("original image",image1)
cv2.imshow("median blur",median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()






















