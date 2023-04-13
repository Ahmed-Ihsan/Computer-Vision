import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Capture.JPG')

median = cv.medianBlur(img,13)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Blurring')
plt.xticks([]), plt.yticks([])
plt.show()
