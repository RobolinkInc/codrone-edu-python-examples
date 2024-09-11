#Python code
from time import sleep
from codrone_edu.drone import *
from codrone_edu.protocol import *

drone = Drone()
drone.pair()


# For demonstration purposes, activate motion calibration
drone.sendCommand(CommandType.ClearBias)
sleep(0.1)
for i in range(10):
    drone.get_error_data() # see motion error state during calibration
    time.sleep(0.5)


drone.close()