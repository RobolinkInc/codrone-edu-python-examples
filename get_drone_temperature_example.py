#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


temperature = drone.get_drone_temperature()
print(temperature)


drone.close()