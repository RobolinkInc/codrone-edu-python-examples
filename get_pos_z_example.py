#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
print(drone.get_pos_z())
drone.land()


drone.close()