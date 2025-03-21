#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

# Sending the drone forward from its takeoff location 0.5 meters moving at 0.5 m/s
drone.send_absolute_position(0.5, 0, 1, 0.5, 0, 0)

# Sending the same command will cause the drone to hover around 
# the same area since this command uses absolute positioning from the takeoff location
drone.send_absolute_position(0.5, 0, 1, 0.5, 0, 0)

drone.land()
drone.close()