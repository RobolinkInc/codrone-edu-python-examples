#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.set_pitch(50)
drone.set_roll(50)
drone.reset_move() # reset the pitch and roll to 0.
drone.land()


drone.close()