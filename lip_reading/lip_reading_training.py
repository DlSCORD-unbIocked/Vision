import cv2
import numpy as np
import face_recognition
import os

currentDir = os.path.dirname(os.path.abspath(__file__)) + "/data/bee.mp4"

cap = cv2.VideoCapture(currentDir)
(major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')

if int(major_ver)  < 3 :
  fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
else :
  fps = cap.get(cv2.CAP_PROP_FPS)

frame_count = int(cap. get(cv2. CAP_PROP_FRAME_COUNT))
print("Frames: " + str(frame_count))
print("Frames per second: " + str(fps))
print("length: " + str(frame_count/fps))
cap.release()

'''
since the data is really large im going to use google collab to train my data set. (>130k frames)
https://colab.research.google.com/drive/1uMZdccUIxVv2jXXPotru_6cDI90D8alp?usp=sharing
'''