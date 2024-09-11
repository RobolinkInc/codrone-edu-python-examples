#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


while True:
    time.sleep(0.1)
    if drone.left_arrow_pressed():
        print("left arrow button has been pressed!")


drone.close()