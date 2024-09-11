#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
print(drone.get_pos_y())
drone.land()


drone.close()