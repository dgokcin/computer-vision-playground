import cv2
from matplotlib import pyplot as plt

# Accentuates differences with local average.
# You use a gaussian smoothing filter and subtract the smoothed version from the original image
# (in a weighted way so the values of a constant area remain constant).
img = cv2.imread('pics/einstein.png')

# blur = cv2.GaussianBlur(img, (5, 5), 0)
sharpened = cv2.addWeighted(img, 2, img, -0.5, 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(sharpened), plt.title('Sharpened')
plt.xticks([]), plt.yticks([])
plt.show()
