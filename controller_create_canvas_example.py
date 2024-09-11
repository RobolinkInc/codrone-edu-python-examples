#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

image = drone.controller_create_canvas() # see controller_draw_canvas for how to draw on this new image object

drone.close()