#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing

drone.controller_draw_point(10, 10) # place a pixel at the (10,10) coordinate


drone.close()