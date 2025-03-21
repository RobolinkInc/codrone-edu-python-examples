#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

# Drone will move to (0.5m, 0, 0.8m) with 0 degree heading.
drone.send_absolute_position(0.5, 0, 0.8, 0.5, 0, 0)

# Drone will move to (0.5m, 0.5m, 0.8m) with 0 degree heading.
drone.send_absolute_position(0.5, 0.5, 0.8, 0.5, 0, 0)

# Drone will move to (0, 0.5m, 0.8m) with 0 degree heading.
drone.send_absolute_position(0, 0.5, 0.8, 0.5, 0, 0)

# Drone will move to (0, 0, 0.8m) with 0 degree heading.
drone.send_absolute_position(0, 0, 0.8, 0.5, 0, 0)

drone.land()
drone.close()