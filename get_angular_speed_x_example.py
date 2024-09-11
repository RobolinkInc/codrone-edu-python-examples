#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


for i in range(100):
    print(drone.get_angular_speed_x())
    time.sleep(0.05)


drone.close()