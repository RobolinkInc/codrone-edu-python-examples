#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


# print the trim values
trim  = drone.get_trim()
print(trim)
print(trim[0])
print(trim[1])


drone.close()