# Atomatically editing pictures

import cv2  
img = cv2.imread("image.jpg") 
cv2.imshow("Original Image",img) 
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) 
cv2.imshow("Edited Image", gray_img) 
cv2.waitKey(0)
