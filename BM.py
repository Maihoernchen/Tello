from djitellopy import Tello
import time
from time import sleep

me = Tello()

me.connect()
print(str(me.get_battery()) + "%")
me.takeoff()

# l/r, f/b, u/d, rl/rrswwwwww

me.send_rc_control(0,0,0,0)

time.sleep(2.0)

me.land()