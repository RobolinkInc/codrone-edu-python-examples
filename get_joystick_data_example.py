#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


while True:
    time.sleep(0.1)
    print(drone.get_joystick_data())


drone.close()