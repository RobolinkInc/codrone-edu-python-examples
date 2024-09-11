#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()

point_list_square = ((10, 10), (30, 10), (30, 30), (10, 30)) # creating a list of coordinates

drone.controller_draw_polygon(point_list_square)


drone.close()