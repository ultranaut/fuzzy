#!/usr/bin/env python

from PIL import Image
import pylab as plb

src = Image.open('sources/fruits.jpg')


"""
do contour
"""
gs = plb.array(src.convert('L'))

plb.figure()
plb.hist(gs.flatten(), 128)

# plb.axis('off')


"""
show original image
"""
im = plb.array(src)

# plb.axis([0, 512, 480, 0])

# x = [50,   50, 100, 100]
# y = [100, 150, 100, 150]

# plb.plbot(x, y, 'ro-')

# plb.plbot(x, y, 'k:')

plb.title('Plotting: "fruits.jpg"')
plb.show()
