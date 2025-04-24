#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()

drone.go("forward", 30, 1) # move forward at 30% power for 1 second
drone.go("backward", 30, 1) # move backward at 30% power for 1 second
drone.go("right", 30, 1) # move right at 30% power for 1 second
drone.go("left", 30, 1) # move left at 30% power for 1 second

drone.land()

drone.close()