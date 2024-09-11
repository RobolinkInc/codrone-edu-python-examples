#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.turn_left() # make a 90 degree left turn.
drone.hover(1) # wait for 1 second in the air
drone.turn_left(30, 3) # make a 30 degree left turn with a 3 second timeout.
drone.land()


drone.close()