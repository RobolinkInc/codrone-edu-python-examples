#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


print(drone.get_x_angle())


drone.close()