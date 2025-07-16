#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.ping() # drone's buzzer beeps and LED blinks a random color 

drone.close()