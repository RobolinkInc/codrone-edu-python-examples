#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# default square parameters (60, 1, 1)
drone.square()
drone.land()


drone.close()