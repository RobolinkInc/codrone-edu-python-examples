#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.set_drone_LED_mode(0, 255, 0, DroneLEDMode.Double_Blink, 10) # the drone's LED will have a green double-blink pattern at speed 10. The 'mode' argument is an Enum

drone.close()