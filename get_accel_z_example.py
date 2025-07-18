#Python code
import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

start_time = time.time() # set initial time, in seconds

# grab and move drone up and down
# loop runs for 20 seconds
while time.time() - start_time < 20:
  print(drone.get_accel_z())
  time.sleep(0.05)

drone.close()