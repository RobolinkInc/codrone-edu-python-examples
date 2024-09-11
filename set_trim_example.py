from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.set_trim(-5, 0) # example: drone is drifting right, so trim to roll left a little bit

time.sleep(1) # Add a time.sleep(1) before takeoff if you're planning to set the trim before takeoff

drone.takeoff()
drone.hover(3)
drone.land()


drone.close()