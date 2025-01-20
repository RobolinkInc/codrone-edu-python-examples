#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


image = drone.controller_create_canvas()  # creates an image object, the canvas

# draws a square on canvas that's 30 x 30px at (0, 0)
drone.controller_draw_square(0, 0, 30, image)

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()