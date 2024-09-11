#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.sendControlWhile(0, 30, 0, 0,1000)  # set pitch to 30 and move for 1000 ms (1 second)
drone.land()


drone.close()