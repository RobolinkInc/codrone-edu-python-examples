#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()
drone.controller_draw_string_align(0, 70, 0, "Hello, world!")


drone.close()