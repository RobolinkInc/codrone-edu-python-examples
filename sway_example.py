#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# default sway parameters (30, 2, 1)
drone.sway()
drone.land()


drone.close()