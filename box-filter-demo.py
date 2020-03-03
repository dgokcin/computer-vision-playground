import cv2
from matplotlib import pyplot as plt

# Replaces each pixel with an average of its neighborhood
img = cv2.imread('pics/opencv_logo.png')

blur = cv2.blur(img, (15, 15))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
