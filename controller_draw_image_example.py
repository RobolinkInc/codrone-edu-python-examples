#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


image = drone.get_image_data("example.png") # where example.png is an image in the same directory as the program

drone.controller_draw_image(image) # draws the image onto the controller's screen

drone.close()