#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


drone.takeoff()
drone.move_distance(0.5, 0.5, 0.25, 1) # move forward 0.5m, left 0.5m, and upward 0.25m simultaneously at 1m/s
drone.move_distance(-0.75, 0, 0, 0.75) # move back 0.75m at 0.75m/s
drone.land()


drone.close()