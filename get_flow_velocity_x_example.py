#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.set_pitch(50)
drone.move(1)
print(drone.get_flow_velocity_x())
drone.land()


drone.close()