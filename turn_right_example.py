#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.turn_right() # make a 90 degree right turn.
drone.hover(1) # wait for 1 second in the air
drone.turn_right(30, 3) # make a 30 degree right turn with a 3 second timeout.
drone.land()


drone.close()