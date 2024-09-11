#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


drone.takeoff()
drone.sendControl(0, 30, 0, 0) # setting pitch to 30
time.sleep(1) # wait for 1 second while the drone is moving forward
drone.land()


drone.close()