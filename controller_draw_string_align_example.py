#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen()
image = drone.controller_create_canvas() # creates an image object, the canvas

# draws string on canvas that is aligned to the right, between x=0 and x=100 at position y=0.
drone.controller_draw_string_align(0, 100, 0, "Hello, world!", image, alignment="right")

drone.controller_draw_canvas(image)  # draw image onto controller screen

drone.close()