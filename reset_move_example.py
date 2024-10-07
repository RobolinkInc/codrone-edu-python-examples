#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.set_pitch(50)
drone.set_roll(50)

drone.move(2)

drone.reset_move() # reset the pitch and roll to 0.

drone.move(2) # after resetting flight variables, move(2) won't move the drone

drone.land()


drone.close()