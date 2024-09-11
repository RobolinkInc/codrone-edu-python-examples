#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# fly forward until a wall is found 50 cm away. run this loop for 10 seconds.
drone.avoid_wall(10, 50)
drone.land()


drone.close()