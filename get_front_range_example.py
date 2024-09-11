#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.hover(3)
distance = drone.get_front_range()
print(distance)
drone.land()


drone.close()