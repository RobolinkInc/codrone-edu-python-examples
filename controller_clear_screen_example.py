#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

image = drone.controller_create_canvas()
drone.controller_draw_rectangle(20, 30, 40, 10, image, 'black')
drone.controller_draw_canvas(image)

time.sleep(3)
drone.controller_clear_screen() # only clears screen, does not modify the image object
time.sleep(3)

image = drone.controller_create_canvas()
drone.controller_draw_string(60, 30, "Hello World!", image)
drone.controller_draw_canvas(image)

drone.close()