#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.turn_degree(90) # drone will turn left 90 degrees
drone.land()


drone.close()