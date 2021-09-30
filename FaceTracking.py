import cv2
from djitellopy import Tello

me = Tello()

cap = cv2.VideoCapture(1)
me.stream_on

while True:
    img = me.get_frame_read().frame
    cv2.imshow("Output", img)
    cv2.waitKey(1)