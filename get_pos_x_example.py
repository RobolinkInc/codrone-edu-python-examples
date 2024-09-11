#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
print(drone.get_pos_x())
drone.land()


drone.close()