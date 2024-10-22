#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()
image = drone.controller_create_canvas() # creates an image object, the canvas

point_list = [(0, 0), (15,15), (30,0)] # list of points that will be connected to draw a polygon

drone.controller_draw_polygon(point_list, image) # forms polygon using list of points

drone.controller_draw_canvas(image)  # draw image onto controller screen



drone.close()