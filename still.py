#!/usr/bin/env python

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fruits.jpg', 1)

cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

blur = cv2.GaussianBlur(img, (75, 1), 0)
cv2.namedWindow('blur', cv2.WINDOW_NORMAL)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# http://stackoverflow.com/a/15074748/1134940
# img = img[:,:,::-1]

# plt.imshow(img, interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()
