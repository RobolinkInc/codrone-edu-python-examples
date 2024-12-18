#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


image = drone.controller_create_canvas()  # creates an image object, the canvas

# draws rectangle starting at (0,0) on canvas with width of 40px and height of 20px
drone.controller_draw_rectangle(0, 0, 40, 20,image)

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()