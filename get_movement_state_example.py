from codrone_edu.drone import *
drone = Drone()

drone.pair()
print(drone.get_movement_state()) # prints "ModeMovement.Ready" after pairing

drone.takeoff()
print(drone.get_movement_state()) # "ModeMovement.Hovering" after takeoff

drone.land()
drone.close()