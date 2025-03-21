#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

# Drone will move to (0, 0, 0.8m) with 180 degree heading.
drone.send_absolute_position(0,0,0.8,0,180,180)

# Drone will move to (0, 0, 0.8m) with 270 degree heading.
drone.send_absolute_position(0,0,0.8,0,270,90)

# Drone will move to (0, 0, 0.8m) with 360 degree heading.
drone.send_absolute_position(0,0,0.8,0,360,90)

# Drone will move to (0, 0, 0.8m) with 450 degree heading.
drone.send_absolute_position(0,0,0.8,0,450,90)

drone.land()
drone.close()