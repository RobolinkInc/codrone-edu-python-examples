#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
print(drone.get_raw_motion_data()) # returns raw motion data
drone.land()


drone.close()