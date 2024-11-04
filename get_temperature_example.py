#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


temperature = drone.get_temperature()
print(temperature)


drone.close()