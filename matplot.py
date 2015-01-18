#!/usr/bin/env python

from PIL import Image
import pylab as pl

src = Image.open('sources/fruits.jpg')


"""
do contour
"""
gs = pl.array(src.convert('L'))

pl.figure()
pl.gray()

pl.contour(pl.flipud(gs), origin='image')
pl.axis('equal')
# pl.axis('off')


"""
show original image
"""
im = pl.array(src)

# pl.axis([0, 512, 480, 0])

# x = [50,   50, 100, 100]
# y = [100, 150, 100, 150]

# pl.plot(x, y, 'ro-')

# pl.plot(x, y, 'k:')

pl.title('Plotting: "fruits.jpg"')
pl.imshow(im)
pl.show()
