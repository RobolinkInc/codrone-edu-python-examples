#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


max_bottom_range = 100
drone.takeoff()
drone.set_throttle(20)
current_bottom_range = drone.get_bottom_range("cm")
while current_bottom_range <= max_bottom_range:
  drone.move()
  current_bottom_range = drone.get_bottom_range("cm")
  print(current_bottom_range)
drone.land()


drone.close()