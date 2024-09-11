#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()


# collect multiple data points
data = drone.get_sensor_data()
for i in range(len(data)):

    print(i, data[i])  # print out each data point



drone.close()