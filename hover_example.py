#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.hover(3)
drone.land()


drone.close()