#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
print(drone.get_z_accel())
drone.land()


drone.close()