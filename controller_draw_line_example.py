#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing

image = drone.controller_create_canvas() # creates an image object, the canvas

drone.controller_draw_line(0, 0, 60, 60, image) # draws a line from (0,0) to (60,60)

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()