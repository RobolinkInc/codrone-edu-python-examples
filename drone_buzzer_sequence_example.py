#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

x = int(input("Enter a number:"))

if x > 5:
  drone.drone_buzzer_sequence("success") # drone's buzzer creates 'success' sound sequence
else:
  drone.drone_buzzer_sequence("error") # drone's buzzer creates 'error' sound sequence

drone.close()