# Python code
from codrone_edu.drone import *

drone = Drone()

drone.pair()

drone.set_roll(30)
drone.set_pitch(40)
drone.set_yaw(50)
drone.set_throttle(60)

move_list = drone.get_move_values() # get_move_values() returns list of flight variables


print("roll:", move_list[0])
print("pitch:", move_list[1])
print("yaw:", move_list[2])
print("throttle:", move_list[3])

drone.close()