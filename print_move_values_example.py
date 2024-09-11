#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.set_pitch(50)
drone.set_roll(50)
drone.print_move_values() # will print pitch and roll at 50 and throttle and yaw at 0
drone.land()


drone.close()