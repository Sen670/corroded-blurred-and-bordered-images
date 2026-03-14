import cv2
import numpy as np
import os

image1 = cv2.imread("lhama2.jpg")
gaussian_blur = cv2.GaussianBlur(image1,(7,7),0)
cv2.imshow("original image",image1)
cv2.imshow("gaussian blur",gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()






















