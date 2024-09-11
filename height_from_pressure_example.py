#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.set_initial_pressure() # Take an initial pressure reading as a reference 

for i in range(300):
    print(drone.height_from_pressure(), " centimeters")
    time.sleep(0.2)

drone.close()