#!/usr/bin/env python

import numpy as np
import cv2


fps = 20
capSize = (1028, 720)
fourcc = cv2.VideoWriter_fourcc('m', 'j', 'p', 'g')
out = cv2.VideoWriter()
success = out.open('output.mov', fourcc, fps, capSize, True)

capture = cv2.VideoCapture(0)
while (capture.isOpened()):
  ret, frame = capture.read()
  if ret is True:
    # frame = cv2.flip(frame, 0)

    # write the frame
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
      break

  else:
    break

capture.release()
out.release()
out = None
cv2.destroyAllWindows()
