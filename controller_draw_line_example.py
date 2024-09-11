#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing

drone.controller_draw_line(0,0, 60, 60)


drone.close()