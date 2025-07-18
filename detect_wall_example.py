#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# if a wall is detected in less than 50cm true will be returned.
if drone.detect_wall():
    print("wall detected!")
else:
    print("no wall detected!")

drone.land()


drone.close()