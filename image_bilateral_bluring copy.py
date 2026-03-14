import cv2
import numpy as np
import os

image1 = cv2.imread("lhama2.jpg")
bilateral_blur = cv2.bilateralFilter(image1,9,75,75)
cv2.imshow("original image",image1)
cv2.imshow("bilateral blur",bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()






















