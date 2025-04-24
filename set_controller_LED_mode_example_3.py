#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.set_controller_LED_mode(255, 255, 255, "rainbow", 10) # the controller's LED will have a rainbow pattern at speed 10. Notice how the RGB values will not affect the rainbow pattern.

drone.close()