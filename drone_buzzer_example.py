#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.drone_buzzer(400, 300)
drone.drone_buzzer(600, 300)

drone.close()