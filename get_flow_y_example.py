#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
drone.set_roll(50)
drone.move(1)
print(drone.get_flow_y())
drone.land()


drone.close()