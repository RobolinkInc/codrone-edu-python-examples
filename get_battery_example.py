#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


battery = drone.get_battery()
print(battery)


drone.close()