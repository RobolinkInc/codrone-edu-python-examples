#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

print(drone.get_y_angle())

drone.close()