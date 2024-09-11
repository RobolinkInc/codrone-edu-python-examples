#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# maintain a distance of 60cm from an object once detected for 10 seconds
drone.keep_distance(10, 60)
drone.land()


drone.close()