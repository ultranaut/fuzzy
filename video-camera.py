#!/usr/bin/env python

import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while (True):
  # Capture frame-by-frame
  ret, frame = capture.read()

  # operate on the frame
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame = frame[:, ::-1, :]
  # blur = cv2.GaussianBlur(frame, (195, 1), 0)

  # display result
  cv2.imshow('frame', frame)

  if cv2.waitKey(16) & 0xFF == ord('q'):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.GaussianBlur(frame, (195, 1), 0)
    cv2.imshow('frame', frame)
    break

# release capture
capture.release()

while (True):
  if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break
