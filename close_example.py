#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.hover(1)
drone.land()


drone.close() # closes connection between controller and program