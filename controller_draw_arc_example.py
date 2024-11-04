#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.controller_clear_screen() # clear screen for drawing
image = drone.controller_create_canvas()  # creates image object, the canvas

arc_list = [(20, 40), (50, 50)]
drone.controller_draw_arc(arc_list, 0, 180, image) # set arc onto image object

drone.controller_draw_canvas(image)  # draw image onto controller screen


drone.close()