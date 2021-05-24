import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('CSE467.png')

blur = cv2.blur(img,(11,11)) #for a 11x11 filter
#blur = cv2.blur(img,(7,7)) #for a 7x7 filter
#blur = cv2.blur(img,(3,3)) #for a 3x3 filter


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
