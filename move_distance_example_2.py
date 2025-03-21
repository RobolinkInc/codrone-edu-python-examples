#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.takeoff()

drone.move_distance(0, 0, 0.5, 0.50) # move up 0.50m at 0.50m/s
drone.move_distance(0, -0.5, 0, 0.50) # move right 0.50m at 0.50m/s
drone.move_distance(0, 0, -0.5, 0.50) # move down 0.50m at 0.50m/s
drone.move_distance(0, 0.5, 0, 0.50) # move left 0.50m at 0.50m/s

drone.land()

drone.close()