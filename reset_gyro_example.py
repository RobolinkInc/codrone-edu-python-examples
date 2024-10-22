#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


print("Before")
print("X angle:", drone.get_angle_x())
print("Y angle:", drone.get_angle_y())
print("Z angle:", drone.get_angle_z())
drone.takeoff()
drone.set_yaw(50)
drone.move(1)
drone.land()
print("After")
print("X angle:", drone.get_angle_x())
print("Y angle:", drone.get_angle_y())
print("Z angle:", drone.get_angle_z())
drone.reset_gyro() 
print("Reset")
print("X angle:", drone.get_angle_x())
print("Y angle:", drone.get_angle_y())
print("Z angle:", drone.get_angle_z())

drone.close()