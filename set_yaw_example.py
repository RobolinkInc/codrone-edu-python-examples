#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# Drone turns left for 1 second with 50 power
drone.set_yaw(50)
drone.move(1) # move command executes the movement for 1 second
drone.land()


drone.close()