import cv2
import numpy as np
from matplotlib import pyplot as plt

# Replaces each pixel with an average of its neighborhood

img = cv2.imread('pics/opencv_logo.png')

# smoothed = cv2.boxFilter(img, 0, (9, 9), img, (1, 1))
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])/9

# applying the sharpening kernel to the input image & displaying it.
smoothed = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(smoothed), plt.title('smoothed')
plt.xticks([]), plt.yticks([])
plt.show()
