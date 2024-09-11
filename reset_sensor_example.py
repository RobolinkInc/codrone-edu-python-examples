#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


print("Before")
print("X angle:", drone.get_x_angle())
print("Y angle:", drone.get_y_angle())
print("Z angle:", drone.get_z_angle())
drone.takeoff()
drone.set_yaw(50)
drone.move(1)
drone.land()
print("After")
print("X angle:", drone.get_x_angle())
print("Y angle:", drone.get_y_angle())
print("Z angle:", drone.get_z_angle())
drone.reset_sensor() 
print("Reset")
print("X angle:", drone.get_x_angle())
print("Y angle:", drone.get_y_angle())
print("Z angle:", drone.get_z_angle())


drone.close()