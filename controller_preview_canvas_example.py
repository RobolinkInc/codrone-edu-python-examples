#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


# NOTE: Everytime controller_create_canvas is called, the preview canvas is reset
image = drone.controller_create_canvas()  # creates an image object, the canvas

arc_list = [(20, 40), (50, 50)]
ellipse_list = [(10, 10), (40, 40)]
chord_list = [(60, 20), (100, 50)]

drone.controller_draw_ellipse(ellipse_list, image) # draw onto image object
drone.controller_draw_arc(arc_list, 0, 180, image)
drone.controller_draw_chord(chord_list, 0, 180, image)

drone.controller_preview_canvas()  # opens a window in computer and displays preview canvas


drone.close()