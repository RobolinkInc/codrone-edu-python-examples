#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


# print the pressure
pressure = drone.get_pressure()
print(pressure)


drone.close()