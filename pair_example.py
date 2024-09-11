#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair() # pair automatically, may not always work
# drone.pair(port_name = 'COM3')    # pair with a specific port


drone.takeoff()
drone.hover(1)
drone.land()


drone.close()