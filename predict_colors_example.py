#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.load_classifier("color_data_file")
color_data = drone.get_color_data()
color = drone.predict_colors(color_data)
print(color)


drone.close()