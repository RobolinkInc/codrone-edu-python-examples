#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.controller_buzzer(400, 300)
drone.controller_buzzer(600, 300)

drone.close()