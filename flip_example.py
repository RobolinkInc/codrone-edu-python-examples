#Python code
import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()

drone.hover(3)
drone.flip("back")  # send flip command
time.sleep(4)  # wait for flip to complete

drone.set_pitch(30) # move forward for 1 second
drone.move(1)

drone.set_pitch(-30) # move backward for 1 second
drone.move(1)

drone.land()


drone.close()