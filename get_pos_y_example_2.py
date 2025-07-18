#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
initial = drone.get_pos_y("cm") # define starting point
drone.set_roll(-15)

# drone moves 100 cm left
while drone.get_pos_y("cm") - initial < 100:
  drone.move()

drone.hover(1)
drone.land()

drone.close()