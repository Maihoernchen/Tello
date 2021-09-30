from djitellopy import Tello
import time
from time import sleep
import cv2

me = Tello()

me.connect()
print(str(me.get_battery()) + "%")

me.streamon()

while True:
    img = me.get_frame_read().frame
    cv2.imshow("Image", img)
    cv2.waitKey(1)