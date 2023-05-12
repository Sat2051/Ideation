import logging

import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('thali.jpeg',0)
edges = cv.Canny(img,100,200)


plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
