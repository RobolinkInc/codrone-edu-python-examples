#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.set_controller_LED(0, 0, 255, 100)

drone.close()