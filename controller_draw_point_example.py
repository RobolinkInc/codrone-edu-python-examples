#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing

image = drone.controller_create_canvas()  # creates an image object, the canvas

drone.controller_draw_point(10, 10, image) # place a pixel at the (10,10) coordinate of canvas

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()