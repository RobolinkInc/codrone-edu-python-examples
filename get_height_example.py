#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


max_height = 100
drone.takeoff()
drone.set_throttle(50)
current_height = drone.get_height("cm")
while current_height <= max_height:
  drone.move()
  current_height = drone.get_height("cm")
  print(current_height)
drone.land()


drone.close()