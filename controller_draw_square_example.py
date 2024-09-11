#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()
drone.controller_draw_square(10, 10, 25)


drone.close()