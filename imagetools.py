#!/usr/bin/env python
"""Helper functions for working with images"""

from PIL import Image
import numpy as np
import pylab as pb

class Picture:

  def __init__(self, path):
    self.src = Image.open(path)
    self.array = np.array(self.src)

  def show(self):
    self.src.show()

def getPic(path):
  src = Image.open(path)
  gray = src.convert('L')
  return src, gray

def plot(src):
  nparray = np.array(src)
  flat = nparray.flatten()
  pb.figure()
  pb.hist(flat, 256)
  # pb.ion()
  # pb.show()

  # pb.figure()
  hist, bins = np.histogram(flat, 256, density=True)
  cdf = hist.cumsum()
  # cdf  = 255 * cdf/cdf[-1]
  pb.plot(bins[:-1], 2500 *cdf, 'r-')
  pb.ion()
  pb.show()


# def resize(src, size):
#   """
#   Resize an array image

#   Args:
#     src: a numpy.ndarray object
#     size: length 2 tuple
#   Returns:
#     resized array
#   """
#   dest = Image.fromarray(np.uint8(src))
#   return np.array(dest.resize(size))


def histeq(src_img, num_bins=256):
  """
  Histogram equalization

  Args:
    src_img: PIL.Image object
    num_bins: number of bins to use for histogram
  Returns:
    2-tuple of equalized image array and cumulative distribution function
  """
  # https://en.wikipedia.org/wiki/Histogram_equalization

  # make array from image
  src_array = np.array(src_img)
  src_flat = src_array.flatten()
  src_shape = src_array.shape

  # get probability density function and bin edges
  hist, bins = np.histogram(src_flat, num_bins, density=True)
  # create cumulative distribution function
  cdf = hist.cumsum()
  # comute equalized values
  cdf = 255 * cdf / cdf[-1]

  # transform src according to cdf
  eqd_flat = np.interp(src_flat, bins[:-1], cdf)
  eqd_array = eqd_flat.reshape(src_shape)
  eqd_image = Image.fromarray(np.uint8(eqd_array))

  # return equalized image and cdf
  return eqd_image, cdf
