import KeyPressModule as kp
from djitellopy import Tello
import time
from time import sleep
import cv2

kp.init()
me = Tello()
me.connect()
print(str(me.get_battery()) + "%")
me.streamon()
a = input()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    if kp.getKey("a"): lr = -50
    elif kp.getKey("d"): lr = 50
    elif kp.getKey("w"): fb = 50
    elif kp.getKey("s"): fb = -50
    elif kp.getKey("r"): ud = 50
    elif kp.getKey("f"): ud = -50
    elif kp.getKey("q"): yv = -50
    elif kp.getKey("e"): yv = 50
    elif kp.getKey("x"): me.land()
    elif kp.getKey("t"): me.takeoff()
    return [lr, fb, ud ,yv]

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (1000,1000))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])

