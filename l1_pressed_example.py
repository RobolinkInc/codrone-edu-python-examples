#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

while True:
    time.sleep(0.1)
    if drone.l1_pressed():
        print("L1 button has been pressed!")


drone.close()