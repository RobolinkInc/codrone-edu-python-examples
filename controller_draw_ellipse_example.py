#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing
image = drone.controller_create_canvas()  # creates an image object, the canvas

ellipse_list = [(10, 10), (40, 40)]
drone.controller_draw_ellipse(ellipse_list, image) # set ellipse onto image object

drone.controller_draw_canvas(image)  # draw image onto controller screen


drone.close()