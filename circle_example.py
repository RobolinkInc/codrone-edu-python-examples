#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# default circle parameters (75, 1)
drone.circle()
drone.land()


drone.close()