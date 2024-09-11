#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# default triangle parameters (60, 1, 1)
drone.triangle()
drone.land()


drone.close()