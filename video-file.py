#!/usr/bin/env python

import numpy as np
import cv2

capture = cv2.VideoCapture('video1.avi')
oldframe = None

def render(frame, freeze=False):
  if freeze is True:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame', frame)
  return frame


while (capture.isOpened()):
  # Capture frame-by-frame
  ret, frame = capture.read()

  ## handle end of file
  if not ret:
    render(oldFrame, True)
    break

  if cv2.waitKey(16) & 0xFF == ord(' '):
    render(frame, True)
    if cv2.waitKey(0) & 0xFF == ord(' '):
      pass

  oldFrame = render(frame)

# release capture
capture.release()

while (True):
  if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break
