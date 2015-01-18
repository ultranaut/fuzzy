#!/usr/bin/env python

from PIL import Image
import numpy as np
import imagetools as imgt

src = Image.open('sources/fruits.jpg')

gray = src.convert('L')
gray.show()

# inverse = np.array(gray)
# inverse = 255 - inverse
# inverse = Image.fromarray(np.uint8(inverse))
# inverse.show()

# mid = np.array(gray)
# mid = 100 + (100.0/255 * mid)
# mid = Image.fromarray(np.uint8(mid))
# mid.show()

# quad = np.array(gray)
# quad = (quad**2.0)/255.0
# quad = Image.fromarray(np.uint8(quad))
# quad.show()

# mod = np.array(gray)
# mod = (mod % 128) * 2
# mod = Image.fromarray(np.uint8(mod))
# mod.show()

# mod = np.array(gray)
# mod = (mod % 128)
# mod = Image.fromarray(np.uint8(mod))
# mod.show()


eqd, cdf = imgt.histeq(np.array(gray))
print eqd
print cdf
eqd = Image.fromarray(np.uint8(eqd))
eqd.show()
