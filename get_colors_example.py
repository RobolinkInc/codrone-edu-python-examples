#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


colors = drone.get_colors()
print(colors)


drone.close()