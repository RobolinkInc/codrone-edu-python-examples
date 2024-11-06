#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


drone.takeoff()
drone.move_forward(distance=50, units="cm", speed=1)
time.sleep(3) # make sure to add a delay so the drone has enough time to fly
drone.land()


drone.close()