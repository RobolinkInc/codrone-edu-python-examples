#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


# This example assumes the "custom_color_data" directory exists
drone.load_classifier("custom_color_data")

color_data = drone.get_color_data()
color = drone.predict_colors(color_data)
print(color)


drone.close()