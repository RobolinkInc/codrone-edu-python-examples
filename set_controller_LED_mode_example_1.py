#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.set_controller_LED_mode(0, 0, 255, "dimming", 10) # the controller's LED will have a blue dimming pattern at speed 10. The 'mode' argument is a string

drone.close()