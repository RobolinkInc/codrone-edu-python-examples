#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()
image = drone.controller_create_canvas() # creates an image object, the canvas

# draws the string "Hello, world!" at (0,0) on canvas
drone.controller_draw_string(0, 0, "Hello, world!", image)

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()