from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(3) # include a hover() or time.sleep() to prevent land() from skipping

drone.land()

drone.close()