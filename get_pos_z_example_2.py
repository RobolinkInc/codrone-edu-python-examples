#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
initial = drone.get_pos_z("cm") # define starting point
drone.set_throttle(50)

# drone moves 50 cm vertically upward
while drone.get_pos_z("cm") - initial < 50:
  drone.move()

drone.hover(1)
drone.land()

drone.close()