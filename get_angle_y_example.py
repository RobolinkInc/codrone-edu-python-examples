#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

print(drone.get_angle_y())

drone.close()