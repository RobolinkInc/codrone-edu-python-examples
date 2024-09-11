#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
data = drone.get_position_data()
print(data)
drone.land()


drone.close()