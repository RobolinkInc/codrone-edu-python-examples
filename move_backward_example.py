#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


drone.takeoff()
drone.move_backward(distance=50, units="cm", speed=1)
drone.land()


drone.close()