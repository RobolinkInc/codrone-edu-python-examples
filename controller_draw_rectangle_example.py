#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()

drone.controller_draw_rectangle(30, 15, 50, 30)


drone.close()