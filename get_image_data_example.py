#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

img_list = ("images/boom.png", "images/flower.png", "images/mario.png", "images/pikachu.jpg", "images/rose.jpg", "images/troll_face.png", "images/pixel_dino.png")

for i in range(len(img_list)):
    img = drone.get_image_data(img_list[i]) # img stores image data
    drone.controller_draw_image(img) # draws image on controller
    time.sleep(1)

drone.close()
