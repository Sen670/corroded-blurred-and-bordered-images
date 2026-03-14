import cv2
import numpy as np
import os

image1 = cv2.imread("manatee.jpg")
image2 = cv2.imread("tree.jpg")
kernel = np.ones((20,20),np.uint8)
erroded_image = cv2.erode(image1,kernel)
erroded_image_2 = cv2.erode(image2,kernel)


cv2.imshow("original image",image1)
cv2.imshow("original image 2",image2)
cv2.imshow("erroded image",erroded_image)
cv2.imshow("erroded image 2",erroded_image_2)
cv2.waitKey()
cv2.destroyAllWindows()






