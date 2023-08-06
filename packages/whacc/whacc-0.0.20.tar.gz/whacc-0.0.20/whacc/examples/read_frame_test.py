import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture("/Users/phil/Dropbox/Autocurator/testing_data/MP4s/AH1026_2014_01_18-1_ANDREW/WDBP_ANM234232-2014_01_18-1_0118_20140123225909859.mp4")

amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)


frame_number = 3000

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
res, frame = cap.read()
plt.figure()

plt.imshow(frame)



frame_number = 1

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
res, frame = cap.read()
plt.figure()
plt.imshow(frame)



cap.set(cv2.CAP_PROP_POS_FRAMES, -9999)




start_frame = 2000

tmp1 = np.arange(start_frame, amount_of_frames)
tmp2 = np.flip(np.arange(0, start_frame))

tmp1
