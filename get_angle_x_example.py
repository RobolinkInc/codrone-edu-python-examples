#Python code
import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

start_time = time.time() # set initial time, in seconds

# tilt the drone left and right
# loop runs for 20 seconds
while time.time() - start_time < 20:
  print(drone.get_angle_x())
  time.sleep(0.05)

drone.close()