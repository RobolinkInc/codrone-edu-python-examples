#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
initial = drone.get_pos_x("cm") # define starting point
drone.set_pitch(15)

# drone moves 100 cm forward
while drone.get_pos_x("cm") - initial < 100:
  drone.move()

drone.hover(1)
drone.land()

drone.close()