import cv2
import numpy as np
from matplotlib import pyplot as plt

# Accentuates differences with local average.
# You use a gaussian smoothing filter and subtract the smoothed version from the original image
# (in a weighted way so the values of a constant area remain constant).

img = cv2.imread('pics/einstein.png')

kernel = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

# applying the sharpening kernel to the input image & displaying it.
sobeled = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(sobeled), plt.title('sobel filter')
plt.xticks([]), plt.yticks([])
plt.show()
